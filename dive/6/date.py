
def check_date(string : str) -> bool:
    def _is_le(year : int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    dmy = [int(x) for x in string.split('.')]

    if len(dmy) != 3: return False
    if dmy[0] < 0 or dmy[0] > 31:   return False
    if dmy[1] < 0 or dmy[1] > 12:   return False
    if dmy[2] < 0 or dmy[2] > 9999: return False
    if dmy[1] in [4, 6, 9, 11] and dmy[0] > 30: return False
    if _is_le(dmy[2]):
        if dmy[1] == 2 and dmy[0] > 29: return False
    else:
        if dmy[1] == 2 and dmy[0] > 28: return False

    return True

if __name__ == "__main__":
    print(check_date("01.21.2025"))