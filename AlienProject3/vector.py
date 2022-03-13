from math import sqrt

class Vector:
    def __init__(self, x=0, y=0): self.x, self.y = x, y
    def __repr__(self): return f'v({self.x},{self.y})'
    def __add__(self, o): return Vector(self.x + o.x, self.y + o.y)
    def __iadd__(self, o): self.x += o.x;  self.y += o.y;  return self
    def __radd_(self, o): return self + o          # what about 3 * v
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

