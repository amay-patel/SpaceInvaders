class GameStats:
    def __init__(self, ai):
        self.settings = ai.settings
        self.reset_stats()
        self.game_active = False
        self.gamescore = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
