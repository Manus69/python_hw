
def fib_check(f):
    store = {}

    def wrap(n : int):
        if n in store: return store[n]
        res = f(n)
        store[n] = res

        return res
    
    return wrap

@fib_check
def fib(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1

    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print(fib(100))