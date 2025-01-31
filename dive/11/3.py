class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def pmt(self):
        return self.w + self.w + self.h + self.h
    
    def area(self):
        return self.w * self.h
    
    def __add__(self, rhs):
        assert(0)

    def __sub__(self, rhs):
        assert(0)

    def __lt__(self, rhs):
        return self.area() < rhs.area()
    
    def __eq__(self, rhs):
        return self.area() == rhs.area()
    
    def __le__(self, rhs):
        return self.area() <= rhs.area()
    