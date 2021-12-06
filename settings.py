class Settings:
    """Class for settings"""

    def __init__(self):
        """Const settings initialization"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 600
        #set background color
        self.bg_color = (30, 30, 30)
        #bullet settings
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (150, 0, 0)
        self.bullets_allowed = 3
        #alien settings
        self.fleet_drop_speed = 10
        #ship settings
        self.ship_limit = 3
        #game speed
        self.initialize_dynamic_settings()
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.button_width = 400
        self.button_height = 100
        self.buttons_positions()
        

    def initialize_dynamic_settings(self):
        """Initialize variable settings"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        #1 - right, -1 - left
        self.fleet_direction = 1
        #score points
        self.alien_points = 20


    def increase_speed(self):
        """game speed faster"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


    def buttons_positions(self):
        """take buttons positions"""
        self.e_button_pos = (self.screen_height / 2) - ((self.button_height / 2) + self.button_height)
        self.m_button_pos = (self.screen_height / 2) + (self.button_height / 2)
        self.h_button_pos = (self.screen_height / 2) + ((self.button_height / 2) + (self.button_height * 2))
        self.button_x_pos = ((self.screen_width / 2) - (self.button_width / 2)) + 40