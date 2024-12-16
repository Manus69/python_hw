import sys

def _repr(x : int, base : int) -> str:
    assert base <= 16 and base >= 2
    assert x >= 0

    digits = "0123456789abcdef"
    rslt = ""

    while True:
        rslt += digits[x % base]
        x //= base

        if x == 0: return rslt[::-1]

def _hex_repr(x : int) -> str:
    return _repr(x, 16)

if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2
        print(_hex_repr(int(sys.argv[1])))
    
    except Exception as e: print(e)
