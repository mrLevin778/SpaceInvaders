"""Main Class"""

import sys

import pygame

from settings import Settings
from ship import Ship

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


    def run_game(self):
        """Main loop of game"""
        while True:
            self._check_events()
            self.ship.update()
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
        elif event.key == pygame.K_q:
            #if pressed key Q, then exit
            sys.exit()


    def _check_keyup_events(self, event):
        """dont move ship, if controller key is up"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False



    def _update_screen(self):
        """refresh screen on loop and how last created screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    #create game copy and run
    ai = AlienInvasion()
    ai.run_game()