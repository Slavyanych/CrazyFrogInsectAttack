import sys
import pygame
from settings import Settings
from frog import Frog

class InsectAttack:
    '''Class for managing resources and game behavior'''
    def __init__(self):
        '''Initializes the game and creates game resources'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Crazy Frog and Insect Attack')
        self.frog = Frog(self)

    def run_game(self):
        '''Start the main game loop'''
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
      '''Handles key presses and mouse event'''
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()

    def _update_screen(self):
        '''Refreshes the screen image and displays the new screen'''
        # The screen is redrawn on each iteretion of the loop
        self.screen.fill(self.settings.bg_color)
        self.frog.blitme()
        # Displaying the last drawn screen
        pygame.display.flip()


if __name__ == '__main__':
    # creating an instance and launching the game
    ai = InsectAttack()
    ai.run_game()