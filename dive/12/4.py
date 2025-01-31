class Product:
    def __init__(self, name, p : int, q : int):
        self.name = name
        self.p = p
        self.q = q

    def __setattr__(self, name, value):
        if name == "p":
            if not (value > 0): raise ValueError
        if name == "q":
            if not (value >= 0): raise ValueError
        
        super().__setattr__(name, value)

    def __str__(self):
        return f"{self.name} {self.p} {self.q}"
