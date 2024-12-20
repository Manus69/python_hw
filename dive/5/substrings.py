
def _subs(string : str):
    for idx in range(len(string)):
        for k in range(1, len(string) - idx + 1):
            yield string[idx:idx + k:] 

def test():
    for s in _subs("0123"):
        print(s)

test()