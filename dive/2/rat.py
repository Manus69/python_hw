from fractions import *

def _parse(string : str) -> Fraction:
    arr = string.split('/')
    if len(arr) != 2: raise ValueError

    try:
        top = int(arr[0])
        bot = int(arr[1])
    except Exception as ex: raise ex

    if bot == 0: raise ValueError

    return Fraction(top, bot)

if __name__ == "__main__":
    try:
        lhs = _parse(input())
        rhs = _parse(input())

        print("sum: ", lhs + rhs)
        print("product: ", lhs * rhs)
    except Exception as ex: print(ex)