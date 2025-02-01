import random
from enum import IntEnum

class Res(IntEnum):
    NONE, LOSS, WIN = range(3)

class Game:
    _p = 13

    def __init__(self, n, filename=".3.txt"):
        self.n = n
        self.current = 0
        self.filename = filename

    def _roll_check(self):
        return random.randint(0, Game._p) == 0

    def _round(self):
        if self._roll_check(): return Res.LOSS

        try:
            x = int(input("Enter a number: "))
            self.current += x
            if self.current >= self.n: return Res.WIN
        except Exception as ex:
            print(ex)

        return Res.NONE

    def play(self):
        while True:
            x = self._round()
            if x == Res.WIN:
                print("You won!")
                break
            if x == Res.LOSS:
                print("You lost!")
                break

            
if __name__ == "__main__":
    game = Game(777)
    game.play()
