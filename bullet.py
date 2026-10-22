import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_game,source,bullet_direction =-1):
        super().__init__() #so this initialize dont overwrite our parent class sprite init
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = self.settings.bullet_colour

        self.rect= pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.bullet_direction = bullet_direction
    
        if self.bullet_direction == -1:
            self.rect.midtop = source.rect.midtop
            self.speed = self.settings.bullet_speed
        else:
            self.rect.midbottom = source.rect.midbottom
            self.speed = self.settings.alien_bullet_speed

        self.y = float(self.rect.y)
    def update(self):
        """Move the bullet up on the screen"""
        self.y += self.settings.bullet_speed * self.bullet_direction
        self.rect.y = self.y

    
    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen,self.colour,self.rect)