import json
from pygame import mixer
import pygame

class GameStats:
    """Stats"""

    def __init__(self, ai_game):
        """initialization"""
        self.settings = ai_game.settings
        self.reset_stats()
        #start game in an inactive state
        self.game_active = False
        self.high_score = 0
        self.high_score_file = 'high_score.json'
        self.bang = pygame.mixer.Sound('sounds/bang.wav')
        self.load_scores()
        self.save_scores()
        

    def reset_stats(self):
        """stats, can be changed"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1


    def play_bang_sound(self):
        """play bang sound"""
        self.bang.play()       


    def load_scores(self):
        """load highscores from json file"""
        try:
            with open(self.high_score_file) as hs:
                self.high_score = json.load(hs)
        except FileNotFoundError:
            with open(self.high_score_file, 'w') as hs:
                json.dump(self.high_score, hs)


    def save_scores(self):
        """save highscores in json file"""
        with open(self.high_score_file, 'w') as hs:
            json.dump(self.high_score, hs)
