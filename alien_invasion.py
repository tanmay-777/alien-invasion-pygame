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
            self.check_events()
            self.ship.update()
            self.update_screen()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == self.settings.right_move:
                    self.ship.moving_right = True
                elif event.key == self.settings.left_move:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == self.settings.right_move:
                    self.ship.moving_right = False
                if event.key == self.settings.left_move:
                    self.ship.moving_left = False

    def update_screen(self):
        pygame.display.flip()
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

