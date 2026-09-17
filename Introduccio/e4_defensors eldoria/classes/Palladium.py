from classes.Combatant import Combatant
from classes.Magic import Magic

class Palladium(Combatant, Magic):
    def __init__(self, name, level, health, strength, mana):
        Combatant.__init__(self, name, level, health, strength)
        Magic.__init__(self, name, level, health, mana)