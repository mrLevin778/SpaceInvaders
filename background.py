import sys
import pygame
from pygame.sprite import Sprite
from pygame import event
from game_stats import GameStats
from settings import Settings

class Background(Sprite):
    """create background"""

    def __init__(self, ai_game):
        super().__init__()
        self.stats = ai_game.stats
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.bg_w = self.settings.screen_width
        self.bg_h = self.settings.screen_height
        #self.clock = pygame.time.Clock()
        #self.y1_pos = self.y_rel
        #self.y2_pos = self.y_rel2

        self.bg_image = pygame.transform.smoothscale(pygame.image.load('images/space.jpg'), (self.bg_w, self.bg_h))
        self.rect = self.bg_image.get_rect()
        self.rect.midtop = self.screen_rect.midtop 
        self.bg_moving()


    def bg_moving(self):
        """"""
        self.clock = pygame.time.Clock()
        pos_y = 0
        speed = 10
        while not sys.exit:
            self.clock.tick(60)
            pos_y += speed
            self.y_rel = pos_y % self.bg_h
            if self.y_rel > 0:
                self.y_rel2 = self.y_rel - self.bg_h
            else:
                break
                #y_rel + self.bg_h
        

    def blit_bg(self):
        """draw background"""
        self.screen.blit(self.bg_image, self.rect)


    def blit_animated(self):
        """"""
        #self.y1_pos = self.y_rel
        #self.y2_pos = self.y_rel2
        self.screen.blit(self.bg_image, (0, self.y_rel))
        self.screen.blit(self.bg_image, (0, self.y_rel2))
