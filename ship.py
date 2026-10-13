import pygame

class Ship:
    def __init__(self, ai_game):
        """Initilize ship and its starting position"""
        #load in the screen dimentional hitbox
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the image file and make its rectangle hitbox
        self.image = pygame.image.load("images/ship.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image,(80,85))
        self.rect = self.image.get_rect()

        #start new ship's center bottom at center bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """Draws the ship"""
        self.screen.blit(self.image,self.rect)
    