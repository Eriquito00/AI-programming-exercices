import random as rd

from classes.tanks.tank import Tank
from classes.projectils.projectil import PR, PP

class ChimpanziniBananini(Tank):
    def __init__(self, name: str):
        super().__init__(
            name=name,
            faction="Chimpanzini Bananini",
            upper_armor=10 * 0.7,
            under_armor=10 * 1.3,
            loader=[PR, PP, PP]
        )

    def rebre_impacte(self, base_damage: float) -> tuple[str, float]:
        if rd.random() < 0.20:
            return "mitigat", base_damage * 0.5
        return "impacte", base_damage