class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def display(self):
        print(f"Parent at {hex(id(self))}, name: {self.name}, age: {self.age}")


    def _add(self, child):
        self.children.append(child)

        return True

    def add_child(self, child):
        return self._add(child) if self.age - child.age <= 16 else False

    def feed(self, child_idx):
        self.children[child_idx].hungry = False

    def calm(self, child_idx):
        self.children[child_idx].calm = True

    def list_children(self):
        for c in self.children: print(c)

class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm = False
        self.hungry = True

    def status(self):
        print(f"{self.name}, calm : {self.calm}, hungry : {self.hungry}")
    
    def __str__(self):
        return f"{self.name}, {self.age} y.o."
