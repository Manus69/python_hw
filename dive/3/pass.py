import sys
import string
import random

def _pass_gen(length : int) -> str:
    pwd = [' '] * length
    pwd[0] = random.choice(string.digits)
    pwd[1] = random.choice(string.punctuation)

    for idx in range(2, length):
        if idx % 2 == 0:
            pwd[idx] = random.choice(string.ascii_lowercase)
        else:
            pwd[idx] = random.choice(string.ascii_uppercase)
    
    random.shuffle(pwd)

    return "".join(pwd)

def main():
    try:
        length = int(sys.argv[1])
        assert length > 2
        
        print(_pass_gen(length))
    except Exception as ex: print(ex)

main()