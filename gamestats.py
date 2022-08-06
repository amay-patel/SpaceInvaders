import json

class GameStats:
    def __init__(self, ai):
        self.settings = ai.settings
        self.reset_stats()
        self.game_active = False
        self.gamescore = 0
        self.highscore = 0
        self.level = 1

    def save_high_scores(self):
        try:
            with open('high_score.json') as f:
                return json.load(f)
        except FileNotFoundError:
            return 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit