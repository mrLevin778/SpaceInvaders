import pygame.font
from settings import Settings


class Button:

    def __init__(self, ai_game, msg):
        """initialize button attributes"""
        self.settings = Settings()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        # set size and other settings
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # create rect button object in position
        self.e_rect = pygame.Rect(self.settings.button_x_pos, self.settings.e_button_pos, self.settings.button_width
                                  , self.settings.button_height)
        self.m_rect = pygame.Rect(self.settings.button_x_pos, self.settings.m_button_pos, self.settings.button_width
                                  , self.settings.button_height)
        self.h_rect = pygame.Rect(self.settings.button_x_pos, self.settings.h_button_pos, self.settings.button_width
                                  , self.settings.button_height)
        # self.rect.position = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """convert text in image and set it in center of button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        if msg == "EASY":
            self.msg_image_rect.center = self.e_rect.center
        if msg == "MEDIUM":
            self.msg_image_rect.center = self.m_rect.center
        if msg == "HARD":
            self.msg_image_rect.center = self.h_rect.center

    def draw_e_button(self):
        """paint buton with text"""
        self.screen.fill(self.button_color, self.e_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def draw_m_button(self):
        """paint buton with text"""
        self.screen.fill(self.button_color, self.m_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def draw_h_button(self):
        """paint buton with text"""
        self.screen.fill(self.button_color, self.h_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
