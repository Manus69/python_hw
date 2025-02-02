class User:
    def __init__(self, name, mail, age):
        self.name = name
        self.mail = mail
        self.age = age

    @property
    def name(self):
        return self.name
    
    @property
    def mail(self):
        return self.mail
    
    @property
    def age(self):
        return self.age
    
    @name.setter
    def name(self, val):
        if not (len(val.split()) >= 2 and all(word[0].isupper() for word in val.split())): raise ValueError()
        self.name = val

    @age.setter
    def age(self, val):
        if not (isinstance(val, int) and val >= 0): raise ValueError()
        self.age = val

    @mail.setter
    def mail(self, val):
        if not "@" in val or "." not in val.split("@")[1]: raise ValueError()

        self.mail = val
    