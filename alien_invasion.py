import sys
from settings import Settings
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """To start the main loop of the game"""

        while True:
            self.check_events()
            self.ship.update()
            self.bullets.update()
            self.update_bullets()
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

    def _create_fleet(self):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        current_x,current_y = alien_width,alien_height

        while current_y < (self.settings.screen_height - (4*alien_height)):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x,current_y)
                current_x +=  2*alien_width
            current_x = alien_width
            current_y += 2*alien_height
            

    def _create_alien(self,x_pos,y_pos):
        new_alien = Alien(self)
        new_alien.x = x_pos
        new_alien.rect.x = x_pos
        new_alien.rect.y = y_pos
        self.aliens.add(new_alien)
            

    def update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
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
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

