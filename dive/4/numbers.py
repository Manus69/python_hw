import sys

def _number_rev(x : int) -> int:
    digits = [int(x) for x in str(x)][::-1]
    val = 0
    for x in digits:
        val *= 10
        val += x

    return val

def main():
    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])

        x = _number_rev(x)
        y = _number_rev(y)
        
        print(_number_rev(x + y))

    except Exception as ex: print(ex)

main()