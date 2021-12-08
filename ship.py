import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Space ship class"""

    def __init__(self, ai_game):
        """Ship init and start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #load ship image and get rect
        self.image = pygame.image.load('images/ship.jpg')
        self.rect = self.image.get_rect()
        #create new ship in bottom and center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        #save float value for ship position in horizontal
        self.x = float(self.rect.x)
        #move indication
        self.moving_right = False
        self.moving_left = False
        

    def update(self):
        """refresh ship position for move indicator"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #refresh object rect in self.x
        self.rect.x = self.x


    def blitme(self):
        """paint ship"""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """set center position for ship"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)