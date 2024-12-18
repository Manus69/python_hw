import sys

def _is_anagram(lhs : str, rhs : str) -> bool:
    if len(lhs) != len(rhs): return False
    
    lhs_letters = sorted([x for x in lhs])
    rhs_letters = sorted([x for x in rhs])

    for x, y in zip(lhs_letters, rhs_letters):
        if x != y: return False
    
    return True

def main():
    try:
        print(_is_anagram(sys.argv[1], sys.argv[2]))
    
    except Exception as ex: print(ex)

main()