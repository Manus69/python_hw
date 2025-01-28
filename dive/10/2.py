import random

_food_price = 10

class House:
    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money
        self.people = []

    def add_tenant(self, person):
        self.people.append(person)

    def buy_food(self, q : int) -> bool:
        val = q * _food_price
        if self.money < val: return False

        self.food += q
        self.money -= val

        return True

    def take_food(self, q):
        if self.food < q: return False

        self.food -= q
        return True

    def add_money(self, q):
        self.money += q

    def check_for_dead(self):
        for p in self.people:
            if p.is_dead(): return p

        return None

    def info(self):
        print(f"House : {hex(id(self))}, food : {self.food}, money : {self.money}, n tenants : {len(self.people)}")


class Person:
    need = 10
    life_threshold = 20
    money_threshold = 50
    food_threshold = 10

    def __init__(self, name, life, house : House):
        self.name = name
        self.house = house
        self.life = life
        self.house.add_tenant(self)

    
    def eat(self) -> bool:
        if self.house.take_food(Person.need):
            self.life += Person.need

            return True
        
        return False

    def work(self, intensity, pay):
        self.life -= intensity
        self.house.add_money(pay)

    def play(self, intensity):
        self.life -= intensity

    def buy_food(self, q : int):
        self.house.buy_food(q)
    
    def is_dead(self):
        return self.life <= 0

    def live(self) -> bool:
        if self.is_dead(): return False
        roll = random.randint(0, 5)

        if      self.life < Person.life_threshold: self.eat()
        if      self.food_threshold < Person.food_threshold: self.buy_food(self.house.money // _food_price)
        elif    self.house.money < Person.money_threshold: self.work(10, 50)
        elif    roll == 0: self.work(10, 50)
        elif    roll == 1: self.eat()
        else:   self.play(5)

        return True

    def die(self, day):
        print(f"{self.name} died at day {day}. RIP")
        self.house.people.remove(self)

if __name__ == "__main__":
    house = House()
    people = [Person("Penelope", 50, house), Person("Alfred", 50, house), Person("Solomon", 50, house)]

    for d in range(0, 355):
        for p in house.people[::-1]:
            if p.live() == False: p.die(d)

