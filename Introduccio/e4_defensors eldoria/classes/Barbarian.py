from classes.Combatant import Combatant

class Barbarian(Combatant):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)