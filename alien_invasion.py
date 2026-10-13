import sys
from settings import Settings
import pygame
from ship import Ship

class AlienInvasion:
    """Overall class to run this game"""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invaders")
        self.ship = Ship(self)

    def run_game(self):
        """To start the main loop of the game"""

        while True:
            self.check_event()
            self.update_screen()
            self.clock.tick(60)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_screen(self):
        pygame.display.flip()
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

