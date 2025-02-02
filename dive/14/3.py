class Rect:
    def __init__(self, w, h):
        """
        >>> r = Rect(3, 4)
        >>> r.area()
        12
        >>> r.prmt()
        14
        """
        self.w = w
        self.h = h

    def set_dim(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h
    
    def prmt(self):
        return self.w + self.w + self.h + self.h
    
import doctest

if __name__ == "__main__":
    doctest.testmod()