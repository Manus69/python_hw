lt = '<'
gt = '>'
eq = '='

def main():
    low = 0
    high = 100
    prev = -1

    while True:
        guess = (low + high) // 2
        if guess == prev:
            print("Error")
            break

        prev = guess
        print("Was your guess %d ? (%s, %s, %s)" % (guess, eq, lt, gt))
        string = input()

        if string == eq:
            break
        elif string == lt:
            high = guess - 1
        elif string == gt:
            low = guess + 1


main()
