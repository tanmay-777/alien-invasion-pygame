import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_game):
        """Initilize ship and its starting position"""
        super().__init__()
        #load in the screen dimentional hitbox
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        #load the image file and make its rectangle hitbox
        self.image = pygame.image.load("images/ship.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image,(80,85))
        self.rect = self.image.get_rect()

        #start new ship's center bottom at center bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom
        #set flag of ship movment to flase
        self.moving_right = False
        self.moving_left = False
        
        self.x = float(self.rect.x) #we dupe the rect x as float into another variable to make minor movmenet

    def blitme(self):
        """Draws the ship"""
        self.screen.blit(self.image,self.rect)

    
    
    
    def update(self):
        """To update the new ship location aka movement of left and right"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x) #to reset the x coords to start tracking ship from middle of screen again
