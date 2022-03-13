import pygame as pg
import sys
from pygame.locals import *
from math import sqrt

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

point = {'x': 10, 'y': 20}
circle = {'center': {'x': 50, 'y': 100}, 'radius': 40, 'color': RED, 'velocity': {'x': 1, 'y': -1}}

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f'[Rectangle, l={self.length :2},w={self.width :2}, area={self.area() :6.2f}, peri={self.peri() :6.2f}]'

    def area(self): return self.length * self.width

    def peri(self): return 2 * (self.length + self.width)

    @staticmethod
    def run_tests():
        print()
        r = Rectangle(length=4, width=2)
        r2 = Rectangle(length=10, width=8)
        print(f' r is {r}')
        print(f'r2 is {r2}')

class Point:
    def __init__(self, x=0, y=0): self.x, self.y = x, y
    def __str__(self): return f'({self.x}, {self.y})'
    def distance_from(self, other):
        delx = self.x - other.x
        dely = self.y - other.y
        return sqrt(delx ** 2 + dely ** 2)
    @staticmethod
    def run_tests():
        print()
        p = Point()
        p2 = Point(x=3, y=-4)
        print(f'p is {p}')
        print(f'p2 is {p2}')
        print(f'{p} is {p.distance_from(p2)} from {p2}')

class Circle:
    def __init__(self, screen, radius, v=Point(1, 1), color=RED, center=Point()):
        self.radius = radius
        self.center = center
        self.color = color
        self.v = v
        self.width, self.height = screen.get_size()  # screen's width and height for boundary test

    def __str__(self):
        return f'[Circle, r={self.radius :2}, ctr={self.center}, area={self.area() :6.2f}, peri={self.peri() :6.2f}]'

    def area(self): return 3.14159 * self.radius ** 2
    def peri(self): return 3.14159 * 2 * self.radius

    def move_to(self, point):
        self.center.x = point.x
        self.center.y = point.y
    def move_by(self, point):
        self.center.x += point.x
        self.center.y += point.y
    def update(self):
        r, x, y = self.radius, self.center.x, self.center.y
        if y + r > self.height or y - r < 0: self.v.y *= -1
        if x - r < 0 or x + r > self.width: self.v.x *= -1
        self.move_by(self.v)
    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.center.x, self.center.y), self.radius, 0)

    @staticmethod
    def run_tests():
        print()
        c = Circle(radius=5)
        c2 = Circle(radius=10, center=Point(99, 99))
        print(f' c is {c}')
        print(f'c2 is {c2}')

        c.move_to(Point(5, 9))
        c2.move_by(Point(-1, -1))
        print('after moving...')
        print(f' c is {c}')
        print(f'c2 is {c2}')

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((500, 400), 0, 32)
        pg.display.set_caption('Python Graphics App from Book')
        self.basic_font = pg.font.SysFont(None, 48)
        # self.circle1 = Circle(radius=40, screen=self.screen, v=Point(1, -1), center=Point(x=460, y=60))
        # self.circle2 = Circle(radius=20, screen=self.screen, v=Point(-1, 1), center=Point(x=300, y=250))
        self.circles = [Circle(radius=10, screen=self.screen,
                        v=Point(-1 if x % 100 == 0 else 1, 1 if x % 100 == 0 else -1),
                        center=Point(x,250)) for x in range(50, 600, 50)]

    def __repr__(self): return f'Polygon Graphics Game'

    def update(self):
        pg.display.update()

    def restart(self): pass
    def level_up(self): pass
    def save(self): pass

    def draw_lines(self):
        pg.draw.line(self.screen, BLUE, (60, 60), (120, 60), 4)
        pg.draw.line(self.screen, BLUE, (120, 60), (60, 120))
        pg.draw.line(self.screen, BLUE, (60, 120), (120, 120), 4)

    def update_circles(self):
      for c in self.circles:
        c.update()
        # self.circle1.update()
        # self.circle2.update()

    def draw_circles(self):
      for c in self.circles:
        c.draw(self.screen)
        # self.circle1.draw(self.screen)
        # self.circle2.draw(self.screen)

    def draw_polygons(self):
        pg.draw.polygon(self.screen, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

    def draw_text(self):
        text = self.basic_font.render('Hello world!', True, WHITE, BLUE)
        text_rect = text.get_rect()
        text_rect.centerx = self.screen.get_rect().centerx
        text_rect.centery = self.screen.get_rect().centery
        pg.draw.rect(self.screen, RED, (text_rect.left - 20,
                                   text_rect.top - 20, text_rect.width + 40, text_rect.height + 40))

        pix_array = pg.PixelArray(self.screen)
        pix_array[480][380] = BLACK
        del pix_array

        self.screen.blit(text, text_rect)

    def draw(self):
        # print(f'drawing in self.draw()')
        self.draw_polygons()
        self.update_circles();  self.draw_circles()
        self.draw_lines()
        self.draw_text()

    def play(self):
        finished = False
        while not finished:
            self.screen.fill(WHITE)
            self.draw()
            self.update()

            for event in pg.event.get():
                if event.type == QUIT:
                    finished = True

        pg.quit()  # game finished
        sys.exit()


def main():
    game = Game()
    game.play()

if __name__ == '__main__':
    main()