import random

_N = 500

class KillError(Exception):
    def __init__(self):
        super().__init__("KE")

class DrunkError(Exception):
    def __init__(self):
        super().__init__("DE")

class CarCrashError(Exception):
    def __init__(self):
        super().__init__("CCE")

class GluttonyError(Exception):
    def __init__(self):
        super().__init__("GE")

class DepressionError(Exception):
    def __init__(self):
        super().__init__("DSE")

def day():
    val = random.randint(0, 7)

    if random.randint(0, 9):
        ex = random.choice([KillError(), DrunkError(), CarCrashError(),
                            GluttonyError(), DepressionError()])

        raise ex

    return val

if __name__ == "__main__":
    n = 0

    with open(".log", "w") as logger:
        while True:
            try:
                n += day()
            except Exception as ex:
                logger.write(f"{ex}\n")        
            if n >= _N: break

        print("done\n")