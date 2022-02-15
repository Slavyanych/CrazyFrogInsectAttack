class Settings:
    '''Class to store all game settings'''
    def __init__(self):
        '''Initializes game settigns'''
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (166, 175, 255)
        self.frog_speed = 2.5
        # projectile parameters
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (155, 65, 65)
        self.bullet_allowed = 5
        # Fly settings
        self.fly_speed = 3.0

