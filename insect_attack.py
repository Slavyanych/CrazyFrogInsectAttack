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
        # # Launching the game in full screen mode
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Crazy Frog and Insect Attack')
        self.frog = Frog(self)

    def run_game(self):
        '''Start the main game loop'''
        while True:
            self._check_events()
            self.frog.update()
            self._update_screen()

    def _check_events(self):
      '''Handles key presses and mouse event'''
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
          elif event.type == pygame.KEYDOWN:
              self._check_keydown_events(event)
          elif event.type == pygame.KEYUP:
              self._check_keyup_events(event)

    def _update_screen(self):
        '''Refreshes the screen image and displays the new screen'''
        # The screen is redrawn on each iteretion of the loop
        self.screen.fill(self.settings.bg_color)
        self.frog.blitme()
        # Displaying the last drawn screen
        pygame.display.flip()

    def _check_keydown_events(self, event):
        '''Responds to key presses'''
        if event.key == pygame.K_RIGHT:
            # Move the frog to the right
            self.frog.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the frog to the left
            self.frog.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        '''Responds to key release'''
        if event.key == pygame.K_RIGHT:
            self.frog.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.frog.moving_left = False



if __name__ == '__main__':
    # creating an instance and launching the game
    ai = InsectAttack()
    ai.run_game()