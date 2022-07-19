class Settings:
    """
    Settings for the size of the window and the background color
    """
    def __init__(self):
        self.screen_length = 1440
        self.screen_height = 790
        self.background_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.bullet_length = 3
        self.bullet_height = 15
        self.bullet_color = (139, 0, 0)
        self.alien_speed = 1.0
        self.fleet_speed = 20
        self.fleet_direction = 1
        self.ship_limit = 3