"""Main Class"""

import sys

import pygame
from pygame import event
from pygame.constants import K_DOWN

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self):
        """Main loop of game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            
    def _check_events(self):
        """mouse and keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)   
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
                
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            #move ship right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #move ship left
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True            
        elif event.key == pygame.K_q:
            #if pressed key Q, then exit
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """dont move ship, if controller key is up"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


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


    def _update_screen(self):
        """refresh screen on loop and how last created screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    #create game copy and run
    ai = AlienInvasion()
    ai.run_game()