import pygame.font

class Button:
    def __init__(self,ai_game,msg,button_colour=(255,20,10)):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200,50
        self.button_colour = button_colour
        self.text_colour = (255,255,255)
        self.font = pygame.font.SysFont(None,70)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self,msg):
        """turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg,True,self.text_colour,self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    def draw_button(self):
        self.screen.fill(self.button_colour,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect) #copy past image the from one to second