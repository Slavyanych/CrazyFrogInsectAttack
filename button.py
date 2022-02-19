import pygame.font

class Button():
    def __init__(self, ai_game, msg):
        ''' Initializes the button attributes '''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Assignment of sizes and properties of buttons
        self.width, self.heigth = 200, 50
        self.button_color = (75, 85, 200)
        self.text_color = (235, 235, 235)
        self.font = pygame.font.SysFont(None, 48)

        # Building a button rect object and aligning it to the center of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.heigth)
        self.rect.center = self.screen_rect.center

        # The button message is created only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        ''' Converts the msg to a rectangle and aligns the text to the center '''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self. msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        ''' Displaying an empty button and displaying a message '''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
