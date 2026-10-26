class GameStats:
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the course of game"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        