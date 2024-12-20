
def _fib(n : int):
    a, b = 0, 1

    for _ in range(n):
        yield a
        next = a + b
        a = b
        b = next

def main():
    fib = _fib(100)
    for x in fib:
        print(x)

main()