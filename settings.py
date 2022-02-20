class Settings:
    '''Class to store all game settings'''
    def __init__(self):
        '''Initializes game settigns'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (166, 175, 255)

        self.frog_limit = 3

        # projectile parameters
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (155, 65, 65)
        self.bullet_allowed = 5

        # Fly settings
        self.flies_drop_speed = 10

        # Game acceleration rate
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        ''' Initializes settings that change during the game '''
        self.frog_speed = 1.5
        self.bullet_speed = 3.0
        self.fly_speed = 1.0

        # flies_direction = 1 means moving to the right; -1 to the left
        self.flies_direction = 1

    def increase_speed(self):
        ''' Increases speed settings'''
        self.frog_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.fly_speed *= self.speedup_scale



