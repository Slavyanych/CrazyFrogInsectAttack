import pygame

class GameStats:
    '''Tracking game statistic'''

    def __init__(self, ai_game):
        '''Initializes statistics'''
        self.settings = ai_game.settings
        self.reset_stats()
        # The game start in an active state
        self.game_active = True

    def reset_stats(self):
        '''Initializes statistics that change during the game'''
        self.frog_left = self.settings.frog_limit