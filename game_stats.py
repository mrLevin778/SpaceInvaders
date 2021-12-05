class GameStats:
    """Stats"""

    def __init__(self, ai_game):
        """initialization"""
        self.settings = ai_game.settings
        self.reset_stats()

        #start game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """stats, can be changed"""
        self.ships_left = self.settings.ship_limit
        self.score = 0