from classes.Character import Character

class Combatant(Character):
    def __init__(self, name, level, health, strength):
        Character.__init__(self, name, level, health)
        self.strength = strength

    def action(self, objective: Character):
        damage = self.strength + (self.level * 2)
        objective.get_damage(damage)