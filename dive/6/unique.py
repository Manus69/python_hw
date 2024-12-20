
def unique(lhs : list, rhs : list) -> list:
    _lhs = set(lhs)
    _rhs = set(rhs)

    return list((_lhs - _rhs).union(_rhs - _lhs))

if __name__ == "__main__":
    print(unique([1, 2, 3], [3, 4, 5]))