from enum import IntEnum
import random

_RPS_STR = "rps"
_GUESS_STR = "guess"
_QUIT_STR = "quit"

class RPS(IntEnum):
    ROCK, PAPER, SCISSORS = range(3)

    def from_str(string : str):
        if      string == "r": return RPS.ROCK
        elif    string == "p": return RPS.PAPER
        elif    string == "s": return RPS.SCISSORS
        else:   raise ValueError

    def roll():
        return RPS(random.randint(0, 2))
    
    def cmp(self, rhs):
        if self.value == rhs.value: return 0
        
        if self.value == RPS.ROCK:
            return 1 if rhs == RPS.SCISSORS else -1
        if self.value == RPS.PAPER:
            return 1 if rhs == RPS.ROCK else -1
        if self.value == RPS.SCISSORS:
            return 1 if rhs == RPS.PAPER else -1
        
        raise ValueError
        

def rps():
    val = RPS.from_str(input("Choose what to play (r, p, s):"))
    roll = RPS.roll()
    print("I play %s" % roll)

    cmp = val.cmp(roll)
    if cmp > 0: print("You won")
    if cmp < 0: print("You lost")
    else : print("Draw")


def guess(low, high):
    target = random.randint(low, high)
    while True:
        val = int(input("Guess the number from %d to %d: " % (low, high)))

        if val == target:
            print("You won")
            break
        if val > target: print("Too high")
        else: print("Too low")

def main():
    while True:
        try:
            mode = input("Choose the game mode (%s, %s, %s): " % (_RPS_STR, _GUESS_STR, _QUIT_STR))
            if      mode == _RPS_STR: rps()
            if      mode == _GUESS_STR: guess(0, 10)
            elif    mode == _QUIT_STR: break
        
        except Exception as ex: print(ex)

main()


