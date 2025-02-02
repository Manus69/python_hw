class ScoreLimError(Exception):
    def __init__(self):
        super().__init__("")

class Score:
    _lim = 1000

    def __init__(self):
        self.score = 0

    def add(self, n):
        if self.score + n >= Score._lim: raise ScoreLimError()

        self.score += n

    def subt(self, n):
        if self.score - n < 0: raise ScoreLimError()

        self.score -= n

    