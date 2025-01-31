import math

class Shape:
    def area(self):
        raise NotImplementedError()
    
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r
    
class Rect(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def area(self):
        return self.w * self.h

class Tri(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h / 2

if __name__ == "__main__":
    c = Circle(1)
    print(c.area())
    t = Tri(17, 13)
    print(t.area())