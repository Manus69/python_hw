
def wc(words : list[str]) -> dict:
    _dict = {}
    
    for w in words:
        _dict[w] = _dict.get(w, 0) + 1
    
    return _dict

if __name__ == "__main__":
    print(wc(["a", "b", "a", "a"]))