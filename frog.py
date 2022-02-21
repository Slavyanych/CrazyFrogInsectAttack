import pygame
from pygame.sprite import Sprite

class Frog(Sprite):
    '''Frog control class'''
    def __init__(self, ai_game):
        '''Initializes the frog and sets its initial position'''
        super(Frog, self).__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loads frog image and gets rectangle
        self.image = pygame.image.load('images/frog_0.bmp')
        self.rect = self.image.get_rect()
        # The frog appears at the bottom of the screen
        self.rect.bottom = self.screen_rect.bottom
        # Saving the real coordinate of the center of the frog
        self.x = float(self.rect.x)
        # Move flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Updates the position of the frog based on th flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.frog_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.frog_speed
        self.rect.x = self.x

    def blitme(self):
        '''Draws a frog in the current position'''
        self.screen.blit(self.image, self.rect)

    def center_frog(self):
        '''Placement of the frog in the center'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


