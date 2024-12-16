import sys

SV = '|'
SH = '-'
SS = ' '

def _form_str(w: int, c: str):
    str = SV + c * (w - 2) + SV
    return str

def _print_rect(w, h):
    print(_form_str(w, SH))
    for _ in range(h - 2):
        print(_form_str(w, SS))
    print(_form_str(w, SH))

if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3
        w = int(sys.argv[1])
        h = int(sys.argv[2])
        assert w > 1 and h > 1
        _print_rect(w, h)
    except: print("Error")
