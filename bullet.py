import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class for bullets managing"""

    def __init__(self, ai_game):
        super().__init__()