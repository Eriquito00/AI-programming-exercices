import random as rd

class Projectil:
    def __init__(self, name: str, damage: float, precision:float):
        self.name = name
        self.damage = damage
        self.precision = precision

    def ha_impactat(self) -> bool:
        return rd.random() <= self.precision

PR = Projectil("PR", 1.0, 0.80)
PP = Projectil("PP", 3.0, 0.35)