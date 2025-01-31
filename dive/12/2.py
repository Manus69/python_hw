class Person:
    def __setattr__(self, name, value):
        if name == "name":
            if not (value and value[0].isupper() and value.isalpha()): raise ValueError
        elif name == "age":
            if not (0 <= value <= 120): raise ValueError
        elif name == "email":
             if "@" not in value: raise ValueError

        super().__setattr__(name, value)

    def __str__(self):
        return f"{self.name} {self.age} {self.email}"
    
    def __init__(self, name : str, age : int, email : str):
        self.name = name
        self.age = age
        self.email = email
    
if __name__ == "__main__":
    x = Person("Jane", 69, "@")
    print(x)