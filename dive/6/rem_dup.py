
def rem_dup(string : str) -> str:
    if len(string) == 0: return string

    letters = [string[0]]

    for idx in range(1, len(string)):
        if string[idx] != letters[-1]: letters.append(string[idx])

    return "".join(letters)

if __name__ == "__main__":
    print(rem_dup("aabbccaa"))
