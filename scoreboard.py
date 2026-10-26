import pygame.font

class Scoreboard:

    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_colour = (57, 255, 20)
        self.font = pygame.font.Font("fonts/press_start_2p.ttf", 30)

        self.prep_score()

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