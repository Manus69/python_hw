import time

def slowdown_factory(t):
    def dec(f):
        def wrap(* args, ** kwargs):
            time.sleep(t)
            res = f(* args, ** kwargs)
            return res
        return wrap
    return dec

slowdown = slowdown_factory(2)

@slowdown
def test0(a : int, b : int) -> int:
    return a + b

if __name__ == "__main__":
    print (test0(1, 69))