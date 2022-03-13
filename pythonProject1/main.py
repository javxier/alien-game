from math import sqrt
import pygame as pg

# def test_pizza():
#     li = ['pepperoni', 'cheese', 'supreme']
#     for el in li:
#         print(f'Do you want a {el} pizza ?')
#     print('Thanks for telling me !')



class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __str__(self):
        return f'({self.x}, {self.y})'

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
    def __init__(self, radius, center=Point()):
        self.radius = radius
        self.center = center
        self.color = color
        self.v = v
        self.width, self.height = screen.get_size()

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
        r, x, y = self.radous, self.center.x, self.center.y

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

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(length=side, width=side)

    def __str__(self):
        return f'[Square, s={self.length :2}, area={self.area() :6.2f}, peri={self.peri() :6.2f}]'

    #def area(self): return self.side ** 2

    #def peri(self): return 4 * self.side

    @staticmethod
    def run_tests():
        print()
        sq = Square(side=4)
        sq2 = Square(side=10)
        print(f' sq is {sq}')
        print(f'sq2 is {sq2}')


def main():
    # test_pizza()
    Circle.run_tests()
    #Rectangle.run_tests()
    #Square.run_tests()
    #Point.run_tests()
    pg.init()


if __name__ == '__main__':
    main()