import pygame

class Ship():
    """Space ship class"""

    def __init__(self, ai_game):
        """Ship init and start position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #create new ship in bottom and center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #save float value for ship position in horizontal
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #move indication
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """refresh ship position for move indicator"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        #refresh object rect in self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """paint ship"""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """set center position for ship"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)