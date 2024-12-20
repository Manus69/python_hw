def _gen_square(x : int):
    for k in range(x + 1):
        yield k ** 2

def main():
    try:
        x = int(input("Enter N max: "))
        for val in _gen_square(x):
            print(val)

        for val in (k ** 2 for k in range(x + 1)):
            print(val)
    
    except Exception as ex: print(ex)
main()