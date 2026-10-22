import pygame

class Settings:
    def __init__(self):
        """Initialize Game's settings"""
        #screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_colour = (48, 50, 58)
        #A and D to move left and right respectively
        self.right_move = pygame.K_d
        self.left_move = pygame.K_a 
        #Q to quit
        self.quit = pygame.K_q
        self.fire = pygame.K_SPACE
        #ship settings
        self.ship_speed = 8
        self.ship_limit = 3

        #bullet's settings
        self.speed = 9 #common speed for both
        self.alien_bullet_speed = 12 
        self.bullet_speed = 9 #12
        self.bullet_width = 300 #3
        self.bullet_height = 5 #18
        self.bullet_colour = (255, 220, 40)
        self.bullet_allowed = 3

        #alien fleet settings
        self.alien_speed = 1
        self.fleet_drop_speed = 200 #10
        self.fleet_direction = 1 #1 means right and -1 means left
        