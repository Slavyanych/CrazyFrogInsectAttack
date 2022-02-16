import pygame
from pygame.sprite import Sprite

class Fly(Sprite):
    '''Class representing one fly'''

    def __init__(self, ai_game):
        '''Initializes the fly and sets its initial positon'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Loading the fly image and assigning the rect attribute
        self.image = pygame.image.load('images/fly.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def update(self):
        '''Move flies to the right or left'''
        self.x += (self.settings.fly_speed * self.settings.flies_direction)
        self.rect.x = self.x

    def check_edges(self):
        '''Returns True if the fly is at the edge af the screen'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True