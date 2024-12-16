import sys
from enum import Enum

class Triangle(Enum):
    NONE = 0,
    REG = 1,
    ISO = 2,
    EQ = 3,

def _classify(sides: list[int]) -> Triangle:
    assert len(sides) == 3
    sides.sort()

    if sides[0] + sides[1] < sides[2]:
        return Triangle.NONE
    
    if sides[0] == sides[1] == sides[2]:
        return Triangle.EQ
    
    if sides[0] == sides[1] or sides[1] == sides[2]:
        return Triangle.ISO

    return Triangle.REG

if __name__ == '__main__':
    try:
        assert len(sys.argv) == 4
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
        tri = _classify([a, b, c])

        if tri == Triangle.NONE:
            print("Not a triangle")
        elif tri == Triangle.EQ:
            print("Equilateral")
        elif tri == Triangle.ISO:
            print("Isosceles")
        else:
            print("Regular")
    except: print("Error")