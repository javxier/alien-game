import pygame as pg
import game_functions as gf
from ship import Ship
from alien import AlienFleet
from settings import Settings
from game_stats import GameStats
from laser import Lasers


class Game:
    RED = (255, 0, 0)

    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.stats = GameStats(game=self)
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        pg.display.set_caption("Alien Invasion")
        self.ship = Ship(game=self)
        self.alien_fleet = AlienFleet(game=self)
        self.lasers = Lasers(game=self)
        self.ship.set_alien_fleet(self.alien_fleet)
        self.ship.set_lasers(self.lasers)

    def restart(self):  pass    # TODO

    def update(self):
        self.ship.update()
        self.alien_fleet.update()
        self.lasers.update()

    def draw(self):
        self.screen.fill(self.bg_color)
        self.ship.draw()
        self.alien_fleet.draw()
        self.lasers.draw()
        pg.display.flip()

    def play(self):
        self.finished = False
        while not self.finished:
            self.update()
            self.draw()
            gf.check_events(game=self)   # exits game if QUIT pressed
        print('GAME OVER!')


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
