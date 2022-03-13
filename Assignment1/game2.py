import pygame as pg
import sys
import game_functions as gf
from vector import Vector
from pygame.sprite import Sprite, Group
from copy import copy
from time import sleep


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (60, 60, 60)

        self.ship_speed_factor = 3
        self.ship_limit = 3

        self.alien_speed_factor = 2
        self.fleet_drop_speed = 8
        self.fleet_direction = Vector(1, 0)

        self.laser_speed_factor = 1
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = 0,238,238


class GameStats:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.reset_stats()
        self.last_ships_left = self.ships_left

    def reset_stats(self): self.ships_left = self.settings.ship_limit
    def ship_hit(self):
        self.ships_left -= 1
        n = self.ships_left
        print(f'SHIP HIT!', end=' ')
        if self.last_ships_left != self.ships_left:
            print(f'{self.ships_left} ship{"s" if n != 1 else ""} left')
            self.last_ships_left = self.ships_left


class AlienFleet:
    def __init__(self, game, v=Vector(1, 0)):
        self.game = game
        self.ship = self.game.ship
        self.settings = game.settings
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()
        self.v = v
        alien = Alien(self.game)
        self.alien_h, self.alien_w = alien.rect.height, alien.rect.width
        self.fleet = Group()
        self.create_fleet()

    def create_fleet(self):
        n_cols = self.get_number_cols(alien_width=self.alien_w)
        n_rows = self.get_number_rows(ship_height=self.ship.rect.height,
                                      alien_height=self.alien_h)
        for row in range(n_rows):
            for col in range(n_cols):
                self.create_alien(row=row, col=col)

    def set_ship(self, ship): self.ship = ship
    def create_alien(self, row, col):
        x = self.alien_w * (2 * col + 1)
        y = self.alien_h * (2 * row + 1)
        alien = Alien(game=self.game, ul=(x, y), v=self.v)
        self.fleet.add(alien)

    def empty(self): self.fleet.empty()
    def get_number_cols(self, alien_width):
        spacex = self.settings.screen_width - 2 * alien_width
        return int(spacex / (2 * alien_width))

    def get_number_rows(self, ship_height, alien_height):
        spacey = self.settings.screen_height - 3 * alien_height - ship_height
        return int(spacey / (2 * alien_height))

    def length(self): return len(self.fleet.sprites())

    def change_v(self, v):
        for alien in self.fleet.sprites():
            alien.change_v(v)

    def check_bottom(self):
        for alien in self.fleet.sprites():
            if alien.check_bottom():
                self.ship.hit()
                break

    def check_edges(self):
        for alien in self.fleet.sprites():
            if alien.check_edges(): return True
        return False

    def update(self):
        delta_s = Vector(0, 0)    # don't change y position in general
        if self.check_edges():
            self.v.x *= -1
            self.change_v(self.v)
            delta_s = Vector(0, self.settings.fleet_drop_speed)
        if pg.sprite.spritecollideany(self.ship, self.fleet) or self.check_bottom():
            self.ship.hit()
        for alien in self.fleet.sprites():
            alien.update(delta_s=delta_s)

    def draw(self):
        for alien in self.fleet.sprites():
            alien.draw()


class Alien(Sprite):
    def __init__(self, game, ul=(0, 100), v=Vector(1, 0)):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.image = pg.image.load('images/alien.bmp')
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = ul
        self.ul = Vector(ul[0], ul[1])   # position
        self.v = v                       # velocity

    def change_v(self, v): self.v = v
    def check_bottom(self): return self.rect.bottom >= self.screen_rect.bottom
    def check_edges(self):
        r = self.rect
        return r.right >= self.screen_rect.right or r.left <= 0

    def update(self, delta_s=Vector(0, 0)):
        self.ul += delta_s
        self.ul += self.v * self.settings.alien_speed_factor
        self.rect.x, self.rect.y = self.ul.x, self.ul.y

    def draw(self):  self.screen.blit(self.image, self.rect)


class Lasers:
    def __init__(self, game):
        self.game = game
        self.alien_fleet = game.alien_fleet
        self.lasers = Group()

    def add(self, laser): self.lasers.add(laser)
    def empty(self): self.lasers.empty()
    def update(self):
        for laser in self.lasers.copy():
            if laser.rect.bottom <= 0: self.lasers.remove(laser)

        collisions = pg.sprite.groupcollide(self.lasers,
                                            self.alien_fleet.fleet,
                                            True, True)
        if self.alien_fleet.length() == 0:
            self.game.restart()

        for laser in self.lasers:
            laser.update()

    def draw(self):
        for laser in self.lasers:
            laser.draw()


class Laser(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.w, self.h = self.settings.laser_width, self.settings.laser_height
        self.ship = game.ship

        self.rect = pg.Rect(0, 0, self.w, self.h)
        self.center = copy(self.ship.center)
        # print(f'center is at {self.center}')
        self.color = self.settings.laser_color
        self.v = Vector(0, -1) * self.settings.laser_speed_factor

    def update(self):
        self.center += self.v
        self.rect.x, self.rect.y = self.center.x, self.center.y

    def draw(self): pg.draw.rect(self.screen, color=self.color, rect=self.rect)


class Ship:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.alien_fleet = None
        self.lasers = None
        self.stats = game.stats
        self.image = pg.image.load('images/ship.bmp')

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.center_bottom()
        self.v = Vector()

    def set_alien_fleet(self, alien_fleet): self.alien_fleet = alien_fleet
    def set_lasers(self, lasers): self.lasers = lasers

    def center_bottom(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = Vector(self.rect.centerx, self.rect.centery)

    def hit(self):
        self.stats.ship_hit()
        if self.stats.ships_left == 0:
            self.game.finished = True
        self.game.restart()

    def moving(self, vector): self.v = vector
    def inc_add(self, other): self.v += other
    def clamp(self):
        rw, rh = self.rect.width, self.rect.height
        srw, srb = self.screen_rect.width, self.screen_rect.bottom
        x, y = self.center.x, self.center.y

        self.center.x = min(max(x, rw/2), srw - rw/2)
        self.center.y = min(max(y, rh/2), srb - rh/2)

    def update(self):
        self.center += self.v * self.settings.ship_speed_factor
        self.clamp()
        self.rect.centerx, self.rect.centery = self.center.x, self.center.y

    def draw(self):
        self.screen.blit(self.image, self.rect)
        # pg.draw.rect(self.screen, Game.RED, self.rect, 1)


class Game:
    RED = (255, 0, 0)

    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.stats = GameStats(game=self)
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        pg.display.set_caption("Invasion de los Aliens")
        self.ship = Ship(game=self)
        self.alien_fleet = AlienFleet(game=self)
        self.lasers = Lasers(game=self)
        self.ship.set_alien_fleet(self.alien_fleet)
        self.ship.set_lasers(self.lasers)

    def restart(self):
        print("restarting game")
        self.lasers.empty()
        self.alien_fleet.empty()
        self.alien_fleet.create_fleet()
        self.ship.center_bottom()
        self.update()
        self.draw()
        sleep(0.5)

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
