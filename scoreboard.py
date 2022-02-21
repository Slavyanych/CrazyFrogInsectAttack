import pygame.font

class Scoreboard():
    ''' Clacc for displaying game informatbon '''
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings
        self.text_color = (0, 10, 100)
        self.font = pygame.font.Font('font/Aprior_Normal.ttf', 36)
        # image preparation
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        ''' Converts the current account into a graphic image '''
        rounded_score = round(self.stats.score, -1)
        score_str = '{:,}'.format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)
        # Invoice in the upper right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10

    def show_score(self):
        ''' Show score on screen '''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    # def check_high_score(self):
    #     ''' Checks if there is a new record '''
    #     if self.stats.score > self.stats.high_score:
    #         self.stats.high_score = self.stats.score
    #         self.prep_high_score()

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_high_score(self):
        ''' Converts the high score into a graphic image '''
        high_score = round(self.stats.high_score, -1)
        high_score_str = '{:,}'.format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.settings.bg_color)
        # Center record
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    # def prep_level(self):
    #     ''' Converts the level to a graphic imaging '''
    #     level_str = str(self.stats.level)
        




