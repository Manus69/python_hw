def dec(f):
    def wrap():
        print("test")
        f()
    
    return wrap

@dec
def test0():
    print("test0")

@dec
def test1():
    test0()
    print("test1")

if __name__ == "__main__":
    # test0()
    test1()