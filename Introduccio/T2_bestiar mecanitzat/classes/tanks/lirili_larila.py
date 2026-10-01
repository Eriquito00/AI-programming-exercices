import random as rd

from classes.tanks.tank import Tank
from classes.projectils.projectil import PR, PP

class LiriliLarila(Tank):
    def __init__(self, name: str):
        super().__init__(
            name=name,
            faction="Lirili Larila",
            upper_armor=10 * 1.3,
            under_armor=10 * 0.7,
            loader=[PP, PR, PR]
        )

    def rebre_impacte(self, base_damage: float) -> tuple[str, float]:
        if rd.random() < 0.20:
            return "esquivat", 0
        return "impacte", base_damage