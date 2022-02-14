import pygame
from pygame.sprite import Sprite

class Fly(Sprite):
    '''Class representing one fly'''

    def __init__(self, ai_game):
        '''Initializes the fly and sets its initial positon'''
        super().__init__()
        self.screen = ai_game.screen
        # Loading the fly image and assigning the rect attribute
        self.image = pygame.image.load('images/fly.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)