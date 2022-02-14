import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Class to control frog projectiles'''

    def __init__(self, ai_game):
        '''Creates a projectile object at the frog's current position'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # Bullet creation at position (0, 0)
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.frog.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        '''Moves bullet up the screen'''
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)




