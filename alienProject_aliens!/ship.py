import pygame as pg
from vector import Vector


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
        self.center = Vector(self.screen_rect.width/2, self.screen_rect.bottom)



    def set_alien_fleet(self, alien_fleet): self.alien_fleet = alien_fleet
    def set_lasers(self, lasers): self.lasers = lasers
    def center_bottom(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = Vector(self.rect.centerx, self.rect.centery)

    def toggle_firing(self): self.firing = not self.firing
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
        if self.frames % 10 == 0 and self.firing:
            self.lasers.fire()
        self.frames += 1

    def draw(self):
        self.screen.blit(self.image, self.rect)
        # pg.draw.rect(self.screen, Game.RED, self.rect, 1)