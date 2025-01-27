def counter(f):
    def wrap(* args, ** kwargs):
        counter.n += 1
        res = f(* args, ** kwargs)

        return res

    counter.n = 0    
    return wrap

@counter
def test(x : int):
    print(x)

if __name__ == "__main__":
    test(-1)
    test(-1)

    print(counter.n)
