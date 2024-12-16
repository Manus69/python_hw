import sys

#a = kb + r
#gcd a b = gcd b r
def _gcd(a : int, b : int) -> int:
    assert (a != 0 or b != 0)

    if a == 0: return b
    if b == 0: return a

    return _gcd(b, a % b)

if __name__ == "__main__":
    assert len(sys.argv) == 3
    print(_gcd(int(sys.argv[1]), int(sys.argv[2])))
