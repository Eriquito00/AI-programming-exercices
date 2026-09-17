from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.Enemy import Enemy

class Character:
    def __init__(self, name, level, health):
        self.nom = name
        self.level = level
        self.health = health

    def info(self):
        return f"Nom: {self.nom}, Nivell: {self.level}, Salut: {self.health}"

    def get_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    @abstractmethod
    def action(self, objective: Enemy):
        pass

    def is_alive(self):
        return self.health > 0