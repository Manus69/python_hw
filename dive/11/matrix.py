import numpy as np

class Mat:
    def __init__(self, * args):
        self.vals = np.array(* args)
    
    def nrows(self):
        return self.vals.shape[0]
    
    def ncols(self):
        return self.vals.shape[1]
    
    def add(self, rhs):
        self.vals += rhs.vals

    def scale(self, c):
        for x in self.vals: x *= c

    def mult(self, rhs):
        self.vals = self.vals.dot(rhs.vals)

    def subt(self, rhs):
        self.vals -= rhs.vals

    def tr(self):
        self.vals.transpose()

    def _dbg(self):
        print(self.vals)


if __name__ == "__main__":
    A = Mat([[1, 0], [0, 1]])
    B = Mat([[np.pi, 1], [-1, 0]])

    
    A._dbg()
    A.mult(B)
    A._dbg()
    B.add(A)
    B.tr()
    B._dbg()