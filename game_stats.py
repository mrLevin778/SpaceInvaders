class GameStats:
    """Stats"""

    def __init__(self, ai_game):
        """initialization"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """stats, can be changed"""
        self.ships_left = self.settings.ship_limit