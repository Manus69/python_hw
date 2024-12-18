
if __name__ == "__main__":
    try:
        lst = [int(x) for x in input().split(" ")]
        print(max(lst))
    except Exception as ex: print(ex)