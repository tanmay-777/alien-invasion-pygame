import sys
from settings import Settings
import pygame
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

from time import sleep

import random


#"spritecollideany" checks collisions for one single sprite against a group, 
#"groupcollide" checks collisions between two entire groups.
#collidepoint: Checks if a single coordinate pair lies inside a rectangle.

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
        self.alien_bullets = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.game_active = False
        self.play_button = Button(self,"Play")
    def run_game(self):
        """To start the main loop of the game"""

        while True:
            self.check_events()
            if self.game_active:
                self.ship.update()
                self.bullets.update()
                self._fire_alien_bullets()
                self.alien_bullets.update()
                self._update_alien_bullets()
                self._update_bullets()
                self._update_aliens()
            self.update_screen()
            self.clock.tick(60)


    def _ship_hit(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1

            self.aliens.empty()
            self.alien_bullets.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()
            #pause
            sleep(0.5)
        else:
            self.game_active = False


    def _fire_alien_bullets(self):
        if not self.aliens:
            return
        if len(self.alien_bullets) < self.settings.bullet_allowed:
            if random.randint(1,60) == 1:
                firing_alien = random.choice(self.aliens.sprites())
                new_bullet = Bullet(self,source=firing_alien,bullet_direction=1)
                self.alien_bullets.add(new_bullet)


    def _update_alien_bullets(self):
        for bullets in self.alien_bullets.copy():
            if bullets.rect.top >= self.settings.screen_height:
                self.alien_bullets.remove(bullets)
                                          
        if pygame.sprite.spritecollideany(self.ship, self.alien_bullets):
            self._ship_hit()

    def _check_alien_bottom_reached(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _check_fleet_edge(self):
        for alien in self.aliens.sprites():
            if alien.edge_check():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _update_aliens(self):
        self._check_fleet_edge()
        self.aliens.update()
        

        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_alien_bottom_reached()

        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            print("SHIP HIT!!")


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self,mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.reset_stats()
            self.game_active = True

            self.aliens.empty()
            self.alien_bullets.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        current_x,current_y = 4*alien_width,alien_height

        while current_y < (self.settings.screen_height - (6*alien_height)):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x,current_y)
                current_x +=  2*alien_width
            current_x = 4*alien_width
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
        for bullet in self.alien_bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        if not self.game_active:
            self.play_button.draw_button()
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
            new_bullet = Bullet(self,source=self.ship, bullet_direction=-1)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()



    def _check_bullet_alien_collision(self):
        #to check for collisions
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,False,True)

        #check if fleet empty, recreate it
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

