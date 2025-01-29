
class Board:
    _size = 3
    _x = 'x'
    _o = 'o'
    __ = '_'

    def row_col_valid(row_col):
        return row_col >= 0 and row_col < Board._size

    def _row_col_idx(row, col):
        return row * Board._size + col
    
    def _idx_row(idx):
        return idx // Board._size
    
    def _idx_col(idx):
        return idx % Board._size

    def __init__(self):
        self.vals = [Board.__] * Board._size * Board._size

    def _from_str(self, _str):
        for k, c in enumerate(_str): self.set_idx(k, c)

    def set(self, row, col, val):
        idx = Board._row_col_idx(row, col)
        self.vals[idx] = val

    def set_idx(self, idx, val):
        self.vals[idx] = val

    def get_idx(self, idx):
        return self.vals[idx]

    def get(self, row, col):
        return self.get_idx(Board._row_col_idx(row, col))

    def display(self):
        for row in range(Board._size):
            for col in range(Board._size):
                x = self.get(row, col)
                print(f"{x} ", end="")
            print()

    def _check_row(self, row, val):
        for col in range(0, Board._size):
            if self.get(row, col) != val: return False

        return True
    
    def _check_col(self, col, val):
        for row in range(0, Board._size):
            if self.get(row, col) != val: return False

        return True

    def _check_ad(self, val):
        for k in range(0, Board._size):
            if self.get(k, Board._size - k - 1) != val: return False

        return True
    
    def _check_md(self, val):
        for k in range(0, Board._size):
            if self.get(k, k) != val : return False

        return True

    def check_win(self, row, col):
        val = self.get(row, col)
        return self._check_row(row, val) or self._check_col(col, val) or self._check_md(val) or self._check_ad(val)

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return self.name

class Game:
    _quit_cmd = "q"
    _move_max = 9

    def __init__(self, p0, p1):
        self.board = Board()
        self.p0 = p0
        self.p1 = p1
        self.move = 0
        self.runs = True

    def _help(self):
        print(f"Type in row col index of cell you want to place {self._turn_val()} in or {Game._quit_cmd} to quit")

    def _turn_val(self):
        return Board._x if self.move % 2 == 0 else Board._o
    
    def _turn_player(self):
        return self.p0 if self.move % 2 == 0 else self.p1
    
    def _turn_coords(_input):
        try:
            row, col = _input.split()
            row = int(row)
            col = int(col)

            assert Board.row_col_valid(row)
            assert Board.row_col_valid(col)

            return row, col
        except Exception as ex: raise ex

    def _turn(self, row, col):
        if self.board.get(row, col) == Board.__:
            val = self._turn_val()
            self.board.set(row, col, val)

        else: raise Exception("Invalid move")

    def turn(self):
        _input = input()

        if _input == Game._quit_cmd: 
            self.runs = False
            return -1, -1
        
        try:
            row, col = Game._turn_coords(_input)
            self._turn(row, col)
            return row, col

        except Exception as ex:
            print(ex)
            self._help()
            return self.turn()

    def check(self, row, col):
        return self.board.check_win(row, col)

    def play(self):
        while True:
            self.display()
            if self.move == Game._move_max: return self._end(True)

            row, col = self.turn()
            if self.runs == False: break
            if self.check(row, col): return self._end(False)

            self.move += 1

    def display(self):
        print()
        self.board.display()
        print()

    def reset(self):
        self.board = Board()
        self.move = 0
    
    def _end(self, draw):
        self.display()

        if draw == True:
            print("Draw")
            return
        
        print(f"{self._turn_player()} won")
        
        player = self._turn_player()
        player.score += 1

if __name__ == "__main__":
    game = Game(Player("player 1", 0), Player("player 2", 0))

    while game.runs == True:
        game.reset()
        game.play()

    print(f"Final score: {game.p0.score} : {game.p1.score}")

