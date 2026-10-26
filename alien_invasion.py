import sys
from settings import Settings
import pygame
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard

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
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Alien Invaders")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.alien_bullets = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.game_active = False
        self.show_difficulty_buttons = False

        self.play_button = Button(self,"Play")

        self.easy_button = Button(self,"Easy",(46, 204, 113))
        self.easy_button.rect.center = self.screen_rect.center
        self.easy_button.rect.y -= 90
        self.easy_button._prep_msg("Easy")
        self.medium_button = Button(self,"Normal",(241, 196, 15))
        self.medium_button.rect.center = self.screen_rect.center
        self.medium_button._prep_msg("Normal")
        self.hard_button = Button(self,"Legend",(231, 76, 60))
        self.hard_button.rect.center = self.screen_rect.center
        self.hard_button.rect.y += 90
        self.hard_button._prep_msg("Legend")
    def run_game(self):
        """To start the main loop of the game"""

        while True:
            self.check_events()
            if self.game_active:
                self.ship.update()
                self.bullets.update()

                # if self.settings.alien_speed > 2:
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
            self.settings.fleet_direction = 1
            #pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


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
                if not self.game_active:
                    if not self.show_difficulty_buttons:
                        self._check_play_button(mouse_pos)
                    else:  
                        self._check_difficulty_buttons(mouse_pos)
            


    def _start_game(self):
        self.stats.reset_stats()
        self.sb.prep_score()
        self.game_active = True
        
        self.aliens.empty()
        self.alien_bullets.empty()
        self.bullets.empty()
        
        self._create_fleet()
        self.ship.center_ship()
        pygame.mouse.set_visible(False)

    def _check_play_button(self,mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active and not self.show_difficulty_buttons:
            self.settings.initialize_dynamic_settings()
            self.show_difficulty_buttons = True
            # self._start_game()

    def _check_difficulty_buttons(self,mouse_pos):
        if not self.game_active and self.show_difficulty_buttons:
            if self.easy_button.rect.collidepoint(mouse_pos):
                self.settings.speedup_scale = 1.1
                self.settings.easy_mode()
                self._start_game()
            elif self.medium_button.rect.collidepoint(mouse_pos):
                self.settings.speedup_scale = 1.2
                self.settings.medium_mode()
                self._start_game()
            elif self.hard_button.rect.collidepoint(mouse_pos):
                self.settings.speedup_scale = 1.35
                self.settings.hard_mode()
                self._start_game()

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
        if self.game_active:
            self.ship.blitme()
            self.sb.show_score()
            self.aliens.draw(self.screen)
        if not self.game_active:
            if not self.show_difficulty_buttons:
                self.play_button.draw_button()
            else: 
                self.easy_button.draw_button()
                self.hard_button.draw_button()
                self.medium_button.draw_button()
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
        elif event.key == self.settings.start_key:
            self._start_game()

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
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()

        #check if fleet empty, recreate it
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

