
def _D(x : float) -> float:
    return x ** 3 - 3 * (x ** 2) - 12 * x + 10

def _root1(f, low, high, eps):
    root = (low + high) / 2
    val = f(root)

    if abs(val) <= eps: return root

    if val * f(low) > 0: return _root1(f, root, high, eps)
    if val * f(high) > 0: return _root1(f, low, root, eps)
    
    raise RuntimeError

def main():
    try:
        d = float(input("Enter D max: "))
        r = _root1(_D, 0, 4, d)
        print(r)

    except Exception as ex: print(ex)

main()