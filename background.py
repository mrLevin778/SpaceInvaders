import pygame
from pygame.sprite import Sprite

class Background(Sprite):
    """create background"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.bg_image = pygame.image.load('images/space.jpg')
        self.rect = self.bg_image.get_rect()
        self.rect.midtop = self.screen_rect.midtop


    def blit_bg(self):
        """draw background"""
        self.screen.blit(self.bg_image, self.rect)

