from decimal import DivisionUndefined
import pygame as pg
import sys, time
from pygame.locals import *
from random import randint
from math import sqrt

# Set up the window.
WINDOWWIDTH = 300
WINDOWHEIGHT = 300

# Set up the colors.
WHITE = (255, 255, 255)
GREY = (90, 90, 90)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
colors = [RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, BLACK]

class Vector:
    def __init__(self, x=0, y=0): self.x, self.y = x, y
    def __repr__(self): return f'v({self.x},{self.y})'
    def __add__(self, o): return Vector(self.x + o.x, self.y + o.y)
    def __radd_(self, o): return self + o
    def __neg__(self): return Vector(-self.x, -self.y)
    def __sub__(self, o): return self + -o
    def __rsub__(self, o): return -(self - o)
    def __mul__(self, k): return Vector(k * self.x, k * self.y)
    def __rmul__(self, k): return self * k
    def __truediv__(self, k): return self * (1.0 / k)
    def dot(self, o): return self.x * o.x + self.y * o.y
    def magnitude(self): return sqrt(self.dot(self))
    def norm(self): return self / self.magnitude()
    def __eq__(self, o): return self.x == o.x and self.y == o.y
    def __ne__(self, o): return not self == o

    @staticmethod
    def run_tests():
        v = Vector()
        v1 = Vector(1, 1)
        v2 = Vector(1, 2)
        k = 2.0
        print(f'v is: {v}')
        print(f'v1 is: {v1}')
        print(f'v2 is: {v2}')
        print(f'{v} + {v2} is: {v + v2}')
        print(f'{v} - {v2} is {v - v2}')
        print(f'{k} * {v2} is: {k * v2}')
        print(f'{v2} * {k} is: {v2 * k}')
        print(f'-{v2} is: {-v2}')
        # v2 / k
        print(f'v2 / k is: {v2 / k}')

        print(f'{v1}.dot({v2}) is: {v1.dot(v2)}')

        print(f'||{v1}|| is: {v1.magnitude()}')
        print(f'||{v2}|| is: {v2.magnitude()}')

        print(f'norm of {v1} is: {v1.norm()}')
        print(f'norm of {v2} is: {v2.norm()}')

        print(f'{v1} == {v2} ? {v1 == v2}')
        print(f'{v1} != {v2} ? {v1 != v2}')

class Box:
    def __init__(self, game, left, top, width, height, color, v=Vector()):
        self.game = game
        self.left, self.top = left, top
        self.width, self.height = width, height
        self.color = color
        self.rect = Rect(left, top, width, height)
        self.v = v

    def update(self):
        self.rect.x += self.v.x
        self.rect.y += self.v.y
        r = self.rect
        if r.top < 0 or r.bottom > WINDOWHEIGHT: self.v.y *= -1
        if r.left < 0 or r.right > WINDOWWIDTH: self.v.x *= -1

        pg.draw.rect(self.game.win, self.color, pg.Rect(r.x, r.y, self.width, self.height))

class Game:
    def __init__(self, nboxes=5):
        pg.init()
        self.win = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
        self.boxes = []
        pg.display.set_caption('Boxxxxxes')
        for i in range(nboxes):
            self.boxes.append(self.random_box())

    def update(self):
        time.sleep(0.04)
        self.win.fill(GREY)
        for b in self.boxes: b.update()

    def random_box(self):
        return Box(
            game=self, left=randint(10, WINDOWWIDTH), top=randint(10, WINDOWHEIGHT),
            width=randint(5, 100), height=randint(5, 100),
            color=colors[randint(0, len(colors) - 1)],
            v=Vector(randint(-3, 3), randint(-3, 3)))

    def play(self):
        finished = False
        while not finished:
            self.update()
            pg.display.update()
            for event in pg.event.get():
                if event.type == QUIT: finished = True

        pg.quit()
        sys.exit()

def main():
    # Vector.run_tests()
    g = Game(nboxes=12)
    g.play()

if __name__ == '__main__':
    main()


#
#
# import pygame as pg
# import sys, time
# from pygame.locals import *
# from random import randint
#
# # Set up direction variables.
# DOWNLEFT = 'downleft'
# DOWNRIGHT = 'downright'
# UPLEFT = 'upleft'
# UPRIGHT = 'upright'
# MOVESPEED = 4
#
# # Set up the window.
# WINDOWWIDTH = 300
# WINDOWHEIGHT = 300
#
# # Set up the colors.
# WHITE = (255, 255, 255)
# GREY = (90, 90, 90)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
# MAGENTA = (255, 0, 255)
# CYAN = (0, 255, 255)
# BLACK = (0, 0, 0)
# colors = [RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, BLACK]
# directions = [DOWNLEFT, DOWNRIGHT, UPLEFT, UPRIGHT]
#
#
# def box(left, top, width, height, color, direction):    # a dictionary, really
#     return { 'rect': pg.Rect(left, top, width, height), 'color': color, 'dir': direction }
#
#
# def random_box():
#     return box(left=randint(10, WINDOWWIDTH), top=randint(10, WINDOWHEIGHT), width=randint(5, 100), height=randint(5, 100),
#                color=colors[randint(0, len(colors) - 1)],
#                direction=directions[randint(0, len(directions) - 1)])
#
#
# def init(nboxes):
#     pg.init()
#
#     win = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
#     pg.display.set_caption('Animation')
#
#     boxes = []
#     for i in range(nboxes):
#         boxes.append(random_box())
#     return win, boxes
#
#
# def update(win, boxes):
#     time.sleep(0.04)
#     win.fill(GREY)
#     for b in boxes:
#         if b['dir'] == DOWNLEFT:
#             b['rect'].left -= MOVESPEED
#             b['rect'].top += MOVESPEED
#         if b['dir'] == DOWNRIGHT:
#             b['rect'].left += MOVESPEED
#             b['rect'].top += MOVESPEED
#         if b['dir'] == UPLEFT:
#             b['rect'].left -= MOVESPEED
#             b['rect'].top -= MOVESPEED
#         if b['dir'] == UPRIGHT:
#             b['rect'].left += MOVESPEED
#             b['rect'].top -= MOVESPEED
#
#         r, v = b['rect'], b['dir']
#         # r is an alias now to b['dir'] UNLESS you write to r, then a copy is made
#         #     and r is now a separate object
#
#         lrdirs = {UPLEFT: UPRIGHT, DOWNLEFT: DOWNRIGHT, UPRIGHT: UPLEFT, DOWNRIGHT: DOWNLEFT}
#         tbdirs = {UPLEFT: DOWNLEFT, UPRIGHT: DOWNRIGHT, DOWNLEFT: UPLEFT, DOWNRIGHT: UPRIGHT}
#
#         if r.top < 0:
#             if v == UPLEFT: b['dir'] = tbdirs[v]     # ok
#             if v == UPRIGHT: b['dir'] = tbdirs[v]
#         if r.bottom > WINDOWHEIGHT:
#             if v == DOWNLEFT: b['dir'] = tbdirs[v]
#             if v == DOWNRIGHT: b['dir'] = tbdirs[v]
#         if r.left < 0:
#             if v == DOWNLEFT: b['dir'] = lrdirs[v]  # ok
#             if v == UPLEFT: b['dir'] = lrdirs[v]
#         if r.right > WINDOWWIDTH:
#             if v == DOWNRIGHT: b['dir'] = lrdirs[v]   # ok
#             if v == UPRIGHT: b['dir'] = lrdirs[v]
#
#         pg.draw.rect(win, b['color'], b['rect'])
#
#
# def main():
#     win, boxes = init(nboxes=20)
#     while True:
#         # Check for the QUIT event.
#         for event in pg.event.get():
#             if event.type == QUIT:
#                 pg.quit()
#                 sys.exit()
#         update(boxes=boxes, win=win)
#         pg.display.update()
#
#
# if __name__ == '__main__':
#     main()