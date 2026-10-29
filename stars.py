from random import choices,randint
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # 1. Rare prominent star (img1)
        img1 = pygame.image.load("images/star.png").convert_alpha()
        img1 = pygame.transform.scale(img1, (35, 35))

        # 2. Common background star (img2) with randomized scale
        img2 = pygame.image.load("images/star_3.png").convert()
        img2.set_colorkey((0,0,0))
        random_size = randint(15, 35)  # Random width & height variation
        img2 = pygame.transform.scale(img2, (random_size, random_size))

        # 5% chance of big star, 95% chance of scaled star
        self.image = choices([img1, img2], weights=[1, 99])[0]

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height