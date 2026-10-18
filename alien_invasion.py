import sys
from settings import Settings
import pygame
from ship import Ship
from bullet import Bullet

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
        self.bullets = pygame.sprite.Group()
    def run_game(self):
        """To start the main loop of the game"""

        while True:
            self.check_events()
            self.ship.update()
            self.bullets.update()
            self.update_screen()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_event(event)
        
            

    def update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()

    def check_keydown_event(self,event):
        if event.key == self.settings.right_move:
            self.ship.moving_right = True
        elif event.key == self.settings.left_move:
            self.ship.moving_left = True
        elif event.key == self.settings.quit:
            sys.exit()
        elif event.key == self.settings.fire:
            self._fire_bullets()

    def check_keyup_event(self,event):
        if event.key == self.settings.right_move:
            self.ship.moving_right = False
        elif event.key == self.settings.left_move:
            self.ship.moving_left = False

    def _fire_bullets(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

