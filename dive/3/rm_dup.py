
def _rm_dup(lst : list) -> list:
    return list(set(lst))

def test():
    lst = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    print(_rm_dup(lst))

if __name__ == "__main__":
    test()