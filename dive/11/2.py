
from enum import IntEnum

class Elem(IntEnum):
    water, air, storm, fire, steam, earth, mud, lightning, dust, lava, shit = range(11)

    def combine(self, elem):
        if _check_pair(self, elem, (Elem.water, Elem.air)) : return Elem.storm
        if _check_pair(self, elem, (Elem.water, Elem.fire)) : return Elem.steam
        if _check_pair(self, elem, (Elem.water, Elem.earth)) : return Elem.mud
        if _check_pair(self, elem, (Elem.air, Elem.fire)) : return Elem.lightning
        if _check_pair(self, elem, (Elem.air, Elem.earth)) : return Elem.dust
        if _check_pair(self, elem, (Elem.fire, Elem.earth)) : return Elem.lava

        return Elem.shit
    
    def __add__(self, value):
        return self.combine(value)

def _check_pair(lhs, rhs, pair):
    return (lhs == pair[0] and rhs == pair[1]) or (lhs == pair[1] and rhs == pair[0]) 

if __name__ == "__main__":
    y = Elem.air
    x = Elem.water

    z = x.combine(y)
    print(z)

    z = Elem.fire + Elem.lava
    print(z)
