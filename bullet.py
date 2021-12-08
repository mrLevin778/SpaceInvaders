import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class for bullets managing"""

    def __init__(self, ai_game):
        """create bullet object in ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #create bullret rect in (0, 0) and set position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        #save bullet position as float
        self.y = float(self.rect.y)

    def update(self):
        """move bullets up"""
        #refresh bullet position
        self.y -= self.settings.bullet_speed
        #refresh rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """bulet draw on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
