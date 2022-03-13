from math import sqrt
import pygame as pg

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f'[Rectangle, l={self.length :2}, w ={self.width :2}, area={self.area() :6.2f}, peri={self.peri() :6.2f}]'

    def area(self): return  self.length * self.width

    def peri(self): return 2 * (self.length + self.width)

    @staticmethod
    def run_test():
        print()
        r = Rectangle(Length = 4, width=2)
        r2 = Rectangle(Length =10,width =8)
        print(f' r is {r},')
        print(f' r2 is {r2}')


def test_pizza():
    li= ['pepperoni', 'cheese','supreme']
    for el in li:
        print(f'Do you want a {el} pizza ?')
    print('Thanks for telling me!')

def main():

   # test_pizza()
  #  test_circle()
   Rectangle.run_test()

   pg.init()

if __name__ == '__main__':
    main()
