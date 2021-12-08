"""Main Class"""
import sys
from time import sleep
import pygame
from pygame import event
from pygame.constants import K_DOWN
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from scoreboard import Scoreboard
from background import Background

class AlienInvasion:
    """Main class, manage resources and gameplay"""

    def __init__(self):
        """Game initialization"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Space Invaders")
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.bg = Background(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #create buttons
        self.easy_button = Button(self, "EASY")
        self.medium_button = Button(self, "MEDIUM")
        self.hard_button = Button(self, "HARD") 


    def run_game(self):
        """Main loop of game"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

            
    def _check_events(self):
        """mouse and keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.save_scores()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)   
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """select level"""
        easy_clicked = self.easy_button.e_rect.collidepoint(mouse_pos)
        medium_clicked = self.medium_button.m_rect.collidepoint(mouse_pos)
        hard_clicked = self.hard_button.h_rect.collidepoint(mouse_pos)
        if easy_clicked and not self.stats.game_active:
            self.settings.speedup_scale = 1.1
            self._start_game()
        if medium_clicked and not self.stats.game_active:
            self.settings.speedup_scale = 1.5
            self._start_game()
        if hard_clicked and not self.stats.game_active:
            self.settings.speedup_scale = 1.7
            self._start_game()


    def _start_game(self):
        """"""
        #reset game stats
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.stats.load_scores()
        self.prep_images()

        #reset bullets and aliens
        self.aliens.empty()
        self.bullets.empty()

        #create new fleet and set ship center
        self._create_fleet()
        self.ship.center_ship()

        #hide mouse
        pygame.mouse.set_visible(False)


    def prep_images(self):
        """prepare images"""
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

                      
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            #move ship right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #move ship left
            self.ship.moving_left = True
        #elif event.key == pygame.K_UP:
        #    self.ship.moving_up = True
        #elif event.key == pygame.K_DOWN:
        #    self.ship.moving_down = True            
        elif event.key == pygame.K_q:
            #if pressed key Q, then exit
            self.stats.save_scores()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """dont move ship, if controller key is up"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        #elif event.key == pygame.K_UP:
        #    self.ship.moving_up = False
        #elif event.key == pygame.K_DOWN:
        #    self.ship.moving_down = False


    def _check_fleet_edges(self):
        """react on edges"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """drop all fleet and change it direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _fire_bullet(self):
        """create new bullet and add it to group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """refresh bullets positions and remove old bullets"""
        #refresh bullets positions
        self.bullets.update()

        #remove old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collision()
    

    def _check_bullet_alien_collision(self):
        """check bullets vs aliens collisiom"""
        collisions = pygame.sprite.groupcollide(    
                    self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            #remove bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            #level up
            self.stats.level += 1
            self.sb.prep_level()


    def _ship_hit(self):
        """event for collision ship vs alien"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #remove aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #create new fleet and fit ship position
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(1.0)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _create_fleet(self):
        """create aliens fleet"""
        #create aliens and calculate aliens quantity in string
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - alien_width
        number_aliens_x = available_space_x // (2 * alien_width)

        #calculate rows quantity, которые помещаются
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                            (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #create full fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        """create alien and set it in string"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _update_aliens(self):
        """проверить, находится ли флот на краю, тогда обновить позиции всех aliens"""
        self._check_fleet_edges()
        #refresh position of all aliens in fleet
        self.aliens.update()

        #check collision ship vs alien
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #check collision alien vs bottom
        self._check_aliens_bottom()


    def _check_aliens_bottom(self):
        """check collision aliens vs bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


    def _draw_buttons(self):
        """draw buttons"""
        self.easy_button.draw_e_button() #easy
        self.medium_button.draw_m_button() #medium
        self.hard_button.draw_h_button() #hard


    def _update_screen(self):
        """refresh screen on loop and how last created screen"""
        self.screen.fill(self.settings.bg_color)
        self.bg.blit_bg()
        if self.stats.game_active:
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)
            #paint score
            self.sb.show_score()
        #paint buttons and static background, if game is inactive
        if not self.stats.game_active:
            self._draw_buttons()
        pygame.display.flip()


if __name__ == '__main__':
    #create game copy and run
    ai = AlienInvasion()
    ai.run_game()