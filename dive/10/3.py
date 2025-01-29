
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

    def set(self, row, col, val):
        idx = Board._row_col_idx(row, col)
        self.vals[idx] = val

    def get_idx(self, idx):
        return self.vals[idx]

    def get(self, row, col):
        return self.get_idx(Board._row_col_idx(row, col))

    def display(self):
        for row in range(Board._size):
            for col in range(Board._size):
                x = self.get(row, col)
                print(x, end="")
            print()

    def _check_row(self, row, val):
        for col in range(0, Board._size):
            if self.get(row, col) != val: return False

        return True
    
    def _check_rows(self, val):
        for row in range(0, Board._size):
            if self._check_row(row, val) == False: return False

        return True
    
    def _check_col(self, col, val):
        for row in range(0, Board._size):
            if self.get(row, col) != val: return False

        return True
    
    def _check_cols(self, val):
        for col in range(0, Board._size):
            if self._check_col(col, val) == False : return False

        return True

    def _check_ad(self, val):
        for row in range(0, Board._size):
            for col in range(Board._size - 1, -1):
                if self.get(row, col) != val: return False

        return True
    
    def _check_md(self, val):
        for row in range(0, Board._size):
            for col in range(0, Board._size):
                if self.get(row, col) != val: return False

        return True

    def check_win(self, val):
        return self._check_rows(val) or self._check_cols(val) or self._check_md(val) or self._check_ad(val)

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Game:
    _quit_cmd = "q"

    def __init__(self, p0, p1):
        self.board = Board()
        self.p0 = p0
        self.p1 = p1
        self.turn = 0
        self.runs = True

    def _help(self):
        print(f"Type in row col index of cell you want to place {self._turn_val} in or {Game._quit_cmd} to quit")

    def _turn_val(self):
        return Board._x if self.turn % 2 == 0 else Board._o
    
    def _turn_player(self):
        return self.p0 if self.turn % 2 == 0 else self.p1
    
    def _turn_coords(_input):
        try:
            row, col = _input.split()
            row = int(row)
            col = int(col)

            assert Board.row_col_valid(row, col)

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
            return
        
        try:
            row, col = Game._turn_coords(_input)

        except Exception as ex:
            print(ex)
            self._help()
    

if __name__ == "__main__":
    brd = Board()
    brd.display()