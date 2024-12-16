import sys

DOT = '.'

def _lhs(val, count):
    string = ""
    while count > 0:
        string += str(val)
        val -= 1
        count -= 1
    
    return string

def _rhs(val, count):
    return _lhs(val, count)[::-1]

def _mid(count):
    return DOT * count

def _row(val, count):
    return _lhs(val, count) + _mid(2 * (val - count)) + _rhs(val, count)

def _pit(val):
    for count in range(1, val + 1):
        print(_row(val, count))

def main():
    try:
        assert len(sys.argv) == 2
        number = int(sys.argv[1])
        _pit(number)

    except Exception as e: print(e)

main()