from abc import abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.Enemy import Enemy

class Character:
    def __init__(self, name, level, health):
        self.nom = name
        self.nivell = level
        self.salut = health

    def info(self):
        return f"Nom: {self.nom}, Nivell: {self.nivell}, Salut: {self.salut}"

    def get_damage(self, damage):
        self.salut -= damage
        if self.salut < 0:
            self.salut = 0

    @abstractmethod
    def action(self, objective: Enemy):
        pass

    def is_alive(self):
        return self.salut > 0