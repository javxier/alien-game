import sys
import pygame as pg
from vector import Vector
from laser import Laser

LEFT, RIGHT, UP, DOWN, STOP = 'left', 'right', 'up', 'down', 'stop'

dirs = {LEFT: Vector(-1, 0),
        RIGHT: Vector(1, 0),
        UP: Vector(0, -1),
        DOWN: Vector(0, 1),
        STOP: Vector(0, 0)}

dir_keys = {pg.K_LEFT: LEFT, pg.K_a: LEFT,
            pg.K_RIGHT: RIGHT, pg.K_d: RIGHT,
            pg.K_UP: UP, pg.K_w: UP,
            pg.K_DOWN: DOWN, pg.K_s: DOWN}

def check_events(game):
    ship = game.ship

    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit()
        elif e.type == pg.KEYDOWN:
            if e.key in dir_keys:
                v = dirs[dir_keys[e.key]]
                ship.inc_add(v)
            elif e.key == pg.K_SPACE:
              game.ship.toggle_firing()
        elif e.type == pg.KEYUP:
            if e.key in dir_keys:
                v = dirs[dir_keys[e.key]]
                ship.inc_add(-v)
            elif e.key == pg.K_SPACE:
              game.ship.toggle_firing()

