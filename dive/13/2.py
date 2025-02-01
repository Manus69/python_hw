class Chat:
    def __init__(self, filename=".chat.txt"):
        self.filename = filename

    def display(self):
        with open(self.filename, "r") as f:
            for x in f.readlines(): print(x)

    def add_msg(self, name, msg):
        with open(self.filename, "a") as f:
            f.write(f"{name} : {msg}")

    def run(self):
        name = input("Enter name: ")
        while True:
            msg = input("Enter your message: ")
            if msg == "/d": self.display()
            if msg == "/q": break

            self.add_msg(name, msg)

if __name__ == "__main__":
    chat = Chat()
    chat.run()