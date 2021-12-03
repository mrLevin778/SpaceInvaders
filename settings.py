class Settings:
    """Class for settings"""

    def __init__(self):
        """Settings initialization"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 600
        #set background color
        self.bg_color = (230, 230, 230)
        #bullet settings
        self.bullet_speed = 1.7
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  #-1 for left

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3