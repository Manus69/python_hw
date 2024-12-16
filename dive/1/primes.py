def _is_prime(x: int):
    if x < 2: return False
    if x == 2: return True

    p = 2
    while p * p <= x:
        if x % p == 0: return False
        p = p + 1
    
    return x % p != 0
    
def main():
    count = 0
    while True:
        try:
            string = input()
            x = int(string)
            if _is_prime(x): count += 1
        except  EOFError:
            print("Number of primes: %d\n" % (count))
            break
        except: print("Invalid input")

main()