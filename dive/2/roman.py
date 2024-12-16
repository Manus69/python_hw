import sys

def _roman_repr(x : int) -> str:
    numerals = {1 : "I", 2 : "II", 3 : "III", 4 : "IV", 5 : "V",
                6 : "VI", 7 : "VII", 8 : "VIII", 9 : "IX", 10 : "X",
                50 : "L", 100 : "C", 1_000 : "M"}

    if x <= 0: raise ValueError
    
    rslt = ""
    keys = list(numerals.keys())[::-1]
    
    for val in keys:
        while True:
            if val > x: break
            rslt += numerals[val]
            x -= val

    return rslt

if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2
        val = int(sys.argv[1])

        print(_roman_repr(val))
    except Exception as ex: print(ex)