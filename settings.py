import pygame

class Settings:
    def __init__(self):
        """Initialize Game's settings"""
        #screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_colour = (13, 17, 23)
        self.right_move = pygame.K_d
        self.left_move = pygame.K_a
        self.ship_speed = 8