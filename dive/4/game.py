from enum import Enum
import random

_RPS_STR = "rps"
_GUESS_STR = "guess"
_QUIT_STR = "quit"

class RPS(Enum):
    ROCK = 0,
    PAPER = 1,
    SCISSORS = 2,

    def from_str(string : str):
        if      string == "r": return RPS.ROCK
        elif    string == "p": return RPS.PAPER
        elif    string == "s": return RPS.SCISSORS
        else:   raise ValueError

    def roll():
        return RPS(random.randint(0, 2))

def rps():
    try:
        val = RPS.from_str(input("Choose what to play (r, p, s):"))
        
    except Exception as ex: raise ex


def main():
    while True:
        try:
            mode = input("Choose the game mode (%s, %s, %s): " % (_RPS_STR, _GUESS_STR, _QUIT_STR))
            if      mode == _RPS_STR: rps()
            elif    mode == _QUIT_STR: break
        
        except Exception as ex: print(ex)

main()


