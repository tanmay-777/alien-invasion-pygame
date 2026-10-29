import pygame.font
from pygame.sprite import Sprite
from pygame.sprite import Group
from ship import Ship

class Scoreboard:

    def __init__(self,ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_colour = (57, 255, 20)
        self.font = pygame.font.Font("fonts/press_start_2p.ttf", 25)
        credit_font = pygame.font.Font("fonts/press_start_2p.ttf", 14)

        # Developer attribution
        self.dev_image = credit_font.render("Made by Tanmay-777", True, self.text_colour)
        self.dev_rect = self.dev_image.get_rect()
        self.dev_rect.bottomright = (self.settings.screen_width - 20, self.settings.screen_height - 35)

        # Music attribution
        self.music_image = credit_font.render('Music "CORE" by Toby Fox', True, self.text_colour)
        self.music_rect = self.music_image.get_rect()
        self.music_rect.bottomright = (self.settings.screen_width - 20, self.settings.screen_height - 15)
        self.prep_high_score()
        self.prep_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 15 + ship_number*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def prep_score(self):
        """To turn score into image ready to be rendered"""
        rounded_score = round(self.stats.score, -1)
        score_str = str(f"SCORE {rounded_score:06d}")
        self.score_image = self.font.render(score_str,True,self.text_colour,self.settings.bg_colour)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 18
        self.score_rect.top = 18

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        
        self.ships.draw(self.screen)

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = str(f"HIGH SCORE {high_score}")
        self.high_score_image = self.font.render(high_score_str,True,self.text_colour,self.settings.bg_colour)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 18

    def check_high_score(self):
        """Check if there is new high score?"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        level_str = str(f"LEVEL {self.stats.level}")
        self.level_image = self.font.render(level_str,True,self.text_colour,self.settings.bg_colour)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 8