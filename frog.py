import pygame

class Frog():
    '''Frog control class'''
    def __init__(self, ai_game):
        '''Initializes the frog and sets its initial position'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Loads frog image and gets rectangle
        self.image = pygame.image.load('images/frog_0.bmp')
        self.rect = self.image.get_rect()
        # The frog appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Draws a frog in the current position'''
        self.screen.blit(self.image, self.rect)


