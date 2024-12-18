
def _max_bin(x : int, y : int) -> int:
    return x if x > y else y

def _max(lst : list) -> int:
    assert len(lst) > 0

    if len(lst) == 1: return lst[0]
    if len(lst) == 2: return _max_bin(lst[0], lst[1])

    return _max_bin(lst[0], _max(lst[1::]))

def main():
    try:
        lst = [int(x) for x in input("Enter space-separated numbers: ").split()]
        print(_max(lst))
    
    except Exception as ex: print(ex)

main()