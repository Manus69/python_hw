
_SUM = "sum"
_MAX = "max"
_MIN = "min"

def _digit_sum(x : int) -> int:
    digits = [_ for _ in str(x)]
    return sum([int(k) for k in digits])

def _max_digit(x : int) -> int:
    digits = [_ for _ in str(x)]
    return max([int(k) for k in digits])

def _min_digit(x : int) -> int:
    digits = [_ for _ in str(x)]
    return min([int(k) for k in digits])

def main():
    while True:
        try:
            val = int(input("Enter a number: "))
            action = input("Enter operation (%s, %s, %s): " % (_SUM, _MAX, _MIN))

            if      action == _SUM: val = _digit_sum(val)
            elif    action == _MAX: val = _max_digit(val)
            elif    action == _MIN: val = _min_digit(val)
            else:   raise ValueError

            print(val)

        except Exception as ex: print(ex)

main()
