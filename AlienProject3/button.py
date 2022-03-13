import pygame.font
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

class Button():
    def __init__(self, screen, msg, ul):
        self.screen = screen

        self.width, self.height = 200, 50
        self.color = GREEN
        self.text_color = WHITE
        self.font = pygame.font.SysFont(None, 48)
        self.ul = ul

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.left, self.rect.top = ul[0], ul[1]

        self.image = self.font.render(msg, True, self.text_color, self.button_color)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.image, self.image_rect)
