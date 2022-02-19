import sys
import pygame
from time import sleep

from settings import Settings
from game_stats import GameStats
from frog import Frog
from bullet import Bullet
from fly import Fly
from button import Button

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

        # Creating an instance for storing game statistics
        self.stats = GameStats(self)

        self.frog = Frog(self)
        self.bullets = pygame.sprite.Group()
        self.flies = pygame.sprite.Group()
        self._create_flies()

        # Creating a Play button
        self.play_button = Button(self, 'Play')



    def run_game(self):
        '''Start the main game loop'''
        while True:
            self._check_events()
            if self.stats.game_active:
                self.frog.update()
                self._update_bullets()
                self._update_flies()
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
          elif event.type == pygame.MOUSEBUTTONDOWN:
              mouse_pos = pygame.mouse.get_pos()
              self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        '''Launches a new game when the Play button is pressed'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset game ststistics
            self.stats.reset_stats()
            self.stats.game_active = True
            # Clear lists of flies and shells
            self.flies.empty()
            self.bullets.empty()
            # Create a new frog and flies
            self._create_flies()
            self.frog.center_frog()
            # Mouse pointer hides
            pygame.mouse.set_visible(False)




    def _update_bullets(self):
        '''Projectile position update. Removing bullets that have gone off the edge of the screen'''
        self.bullets.update()

        # Removing bullets that have gone off the edge of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullets_fly_collisions()

    def _check_bullets_fly_collisions(self):
        '''Handing bullets collisions with flies'''
        # Check bullet impact
        collisions = pygame.sprite.groupcollide(self.bullets, self.flies, False, True)

        if not self.flies:
            self.bullets.empty()
            self._create_flies()


    def _update_flies(self):
        '''Update the positions of all flies'''
        self._chack_flies_adges()
        self.flies.update()

        # Checking collisions "fly - frog"
        if pygame.sprite.spritecollideany(self.frog, self.flies):
            self._frog_hit()

        # Check if the flies have reached the bottom edge
        self._check_flies_bottom()


    def _frog_hit(self):
        ''' Processing collisions "fly - frog" '''
        if self.stats.frog_left > 0:
            self.stats.frog_left -= 1
            # Clearing lists
            self.flies.empty()
            self.bullets.empty()
            # Creation of a new group of files. Placement of the frog in the center
            self._create_flies()
            self.frog.center_frog()
            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_flies_bottom(self):
        '''Checks if the flies have reached the bottom of the screen'''
        screen_rect = self.screen.get_rect()
        for fly in self.flies.sprites():
            if fly.rect.bottom >= screen_rect.bottom:
            #The same thing happens as in a collision with a frog
                self._frog_hit()
                break

    def _create_flies(self):
        '''Create the bunch of flies'''
        # creste the fly
        fly = Fly(self)
        fly_widht, fly_height = fly.rect.size
        available_space_x = self.settings.screen_width - (2 * fly_widht)
        number_flies_x = available_space_x // (2 * fly_widht)

        # Determines the number of rows that fit on the screen
        frog_height = self.frog.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * fly_height) - frog_height)
        number_rows = available_space_y // (2 * fly_height)

        # Create the bunch of flies
        for row_number in range(number_rows):
            # Create the first row of flies
            for fly_number in range(number_flies_x):
                self._create_fly(fly_number, row_number)


    def _create_fly(self, fly_number, row_number):
        '''Create a fly and add it to the row'''
        fly = Fly(self)
        fly_widht, fly_heigth = fly.rect.size
        fly.x = fly_widht + 2 * fly_widht * fly_number
        fly.rect.x = fly.x
        fly.rect.y = fly.rect.height + 2 * fly.rect.height * row_number
        self.flies.add(fly)


    def _chack_flies_adges(self):
        '''Reacts when reaching the edge of the screen'''
        for fly in self.flies.sprites():
            if fly.check_edges():
                self._change_flies_direction()
                break

    def _change_flies_direction(self):
        '''Lowers and reverses flies'''
        for fly in self.flies.sprites():
            fly.rect.y += self.settings.flies_drop_speed
        self.settings.flies_direction *= -1


    def _update_screen(self):
        '''Refreshes the screen image and displays the new screen'''
        # The screen is redrawn on each iteretion of the loop
        self.screen.fill(self.settings.bg_color)
        self.frog.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.flies.draw(self.screen)
        # The Play button is displayed if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        '''Responds to key release'''
        if event.key == pygame.K_RIGHT:
            self.frog.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.frog.moving_left = False

    def _fire_bullet(self):
        '''creating a new bullet and including it in a group af bullets'''
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)





if __name__ == '__main__':
    # creating an instance and launching the game
    ai = InsectAttack()
    ai.run_game()