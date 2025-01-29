class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, ws, wl):
        super().__init__(name)
        self.ws = ws
        self.wl = wl

class Fish(Animal):
    def __init__(self, name, md):
        super().__init__(name)
        self.md = md

class Mammal(Animal):
    def __init__(self, name, w):
        super().__init__(name)
        self.w = w

def get_animal(tstr, * args) -> Animal:
    types = {"bird" : Bird, "fish" : Fish, "mammal" : Mammal}

    if tstr in types: return types[tstr](* args)

    raise ValueError()
