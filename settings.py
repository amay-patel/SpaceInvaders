class Settings:
    """
    Settings for the size of the window and the background color
    """
    def __init__(self):
        self.screen_length = 1440
        self.screen_height = 790
        self.background_color = (230, 230, 230)
        self.bullet_length = 3
        self.bullet_height = 15
        self.bullet_color = (139, 0, 0)
        self.fleet_speed = 20
        self.ship_limit = 3
        self.speedup_scale = 1.2
        self.difficulty_level = 'medium'
        self.initsettings()

    def initsettings(self):
        if self.difficulty_level == 'easy':
            self.ship_limit = 5
            self.ship_speed = 0.75
            self.bullet_speed = 1.5
            self.alien_speed = 0.5
        elif self.difficulty_level == 'medium':
            self.ship_limit = 3
            self.ship_speed = 1.5
            self.bullet_speed = 3.0
            self.alien_speed = 1.0
        elif self.difficulty_level == 'difficult':
            self.ship_limit = 2
            self.ship_speed = 3.0
            self.bullet_speed = 6.0
            self.alien_speed = 2.0

        self.fleet_direction = 1

    def adjust_settings(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

    def determine_difficulty(self, curr_diff):
        if curr_diff == 'easy':
            print('easy')
        elif curr_diff == 'medium':
            pass
        elif curr_diff == 'difficult':
            pass