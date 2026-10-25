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
        self.start_key = pygame.K_p
        #Q to quit
        self.quit = pygame.K_q
        self.fire = pygame.K_SPACE
        #ship settings
        
        self.ship_limit = 3

        #bullet's settings
        self.speed = 9 #common speed for both
        self.alien_bullet_speed = 12 
        
        self.bullet_width = 3 #3
        self.bullet_height = 18 #18
        self.bullet_colour = (255, 220, 40)
        self.bullet_allowed = 3

        #alien fleet settings
        
        self.fleet_drop_speed = 48 #10
        
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.alien_speed = 1.5
        self.ship_speed = 7.0
        self.bullet_speed = 9.0 #12

        self.fleet_direction = 1 #1 means right and -1 means left

    def easy_mode(self):
        self.alien_speed = 1.1
        self.ship_speed = 8
        self.bullet_speed = 10.0

    def medium_mode(self):
        self.alien_speed = 1.5
        self.ship_speed = 7.0
        self.bullet_speed = 9.0 

    def hard_mode(self):
        self.alien_speed = 2.2
        self.ship_speed = 7.0
        self.bullet_speed = 9

    def increase_speed(self):
        self.alien_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale