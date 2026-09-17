from classes.Character import Character

class Magic(Character):
    MANA_COST = 5

    def __init__(self, name, level, health, mana):
        super().__init__(name, level, health)
        self.mana = mana

    def action(self, objective: Character):
        if self.check_mana():
            damage = 10 + (self.level * 2)
            self.mana -= self.MANA_COST
            objective.get_damage(damage)


    def heal(self):
        if self.check_mana():
            heal = 10 + self.level
            self.mana -= self.MANA_COST
            self.health += heal

    def check_mana(self) -> bool:
        return self.mana >= self.MANA_COST