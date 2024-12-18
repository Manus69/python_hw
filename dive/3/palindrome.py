import sys

def _is_palindrome(string : str) -> bool:
    if len(string) < 2: return True
    if string[0] != string[-1]: return False

    return _is_palindrome(string[1:-1])

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2: raise RuntimeError
        print(_is_palindrome(sys.argv[1]))
    
    except Exception as ex: print(ex)