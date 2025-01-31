
class Stack:
    def __init__(self):
        self.vals = []

    def push(self, val):
        self.vals.append(val)

    def pop(self):
        return self.vals.pop()

    def __str__(self):
        cstr = ""
        for x in self.vals:
            cstr += x.__str__()

        return cstr
    
class Task:
    def __init__(self, cstr, prio):
        self.cstr = cstr 
        self.prio = prio

    def __str__(self):
        return f"{self.cstr} "

    def __hash__(self):
        return self.prio
    
class Manager:

    def __init__(self):
        self.stacks = dict()

    def add_task(self, val : Task):
        if val.prio not in self.stacks:
            self.stacks[val.prio] = Stack()
        
        self.stacks[val.prio].push(val)

    def __str__(self):
        cstr = ""
        for prio in sorted(self.stacks.keys()):
            cstr += prio.__str__()
            cstr += " : "
            cstr += self.stacks[prio].__str__()
        return cstr

if __name__ == "__main__":
    mn = Manager()
    mn.add_task(Task("eat", 0))
    mn.add_task(Task("sleep", 0))
    mn.add_task(Task("shit", 27))

    print(mn)