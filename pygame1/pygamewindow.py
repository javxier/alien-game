import pygame as pg
import sys
from pygame.locals import *


class Game:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((500, 400), 0, 32)
        pg.display.set_caption('Python Graphics App from IYOG w/ Python')
        self.basic_font = pg.font.SysFont(None, 48)

    def __repr__(self): return f'Polygon Graphics Game'

    def update(self):
        pg.display.update()

    def restart(self): pass
    def level_up(self): pass
    def save(self): pass

    def draw_lines(self):
        pg.draw.line(self.screen, Game.BLUE, (60, 60), (120, 60), 4)
        pg.draw.line(self.screen, Game.BLUE, (120, 60), (60, 120), 4)
        pg.draw.line(self.screen, Game.BLUE, (60, 120), (120, 120), 4)

    # def update_circles(self):
    #     self.circle.x += 10
    #     self.circle.y += 10
    #     self.ellipse.x += 1
    #     self.ellipse.y += 1

    def draw_circles(self):
        pg.draw.circle(self.screen, Game.BLUE, (400, 60), 40, 0)
        pg.draw.ellipse(self.screen, Game.RED, (300, 250, 40, 80), 5)

    def draw_polygons(self):
        pg.draw.polygon(self.screen, Game.GREEN, ((146, 0), (291, 106),
                                    (236, 277), (56, 277), (0, 106)))

    def draw_text(self):
        text = self.basic_font.render('Hello world!', True, Game.WHITE, Game.BLUE)
        text_rect = text.get_rect()
        text_rect.centerx = self.screen.get_rect().centerx
        text_rect.centery = self.screen.get_rect().centery
        pg.draw.rect(self.screen, Game.RED, (text_rect.left - 20, text_rect.top -20,
                                             text_rect.width +40, text_rect.height + 40))

        pix_array = pg.PixelArray(self.screen)
        pix_array[480][380] = Game.BLACK
        del pix_array

        self.screen.blit(text, text_rect)

    def draw(self):
        self.draw_polygons()
        self.draw_circles()
        self.draw_lines()
        self.draw_text()

    def play(self):
        finished = False
        while not finished:
            for event in pg.event.get():
                self.screen.fill(Game.WHITE)
                self.draw()
                self.update()

                if event.type == QUIT:
                    finished = True

        pg.quit()
        sys.exit()

def main():
    game = Game()
    game.play()

if __name__ == '__main__':
    main()