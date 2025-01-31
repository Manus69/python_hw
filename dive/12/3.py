class Book:
    _count = 0

    def __new__(cls, * args, ** kwargs):
        ins = super().__new__(cls)
        ins.id = cls._count
        cls._count += 1

        return ins
    
    def __init__(self, title, auth):
        self.title = title
        self.auth = auth

    def __str__(self):
        return f"{self.title} by {self.auth}"
    
if __name__ == "__main__":
    x = Book("title", "author")
    print(x)