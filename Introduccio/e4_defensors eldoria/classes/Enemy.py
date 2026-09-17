from __future__ import annotations
import random as rd

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.Character import Character

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def info(self):
        return f"Name: {self.name}, Health: {self.health}"

    def is_alive(self):
        return self.health > 0

    def get_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def phisical_attack(self, objective: Character):
        damage = rd.randint(15,35)
        objective.get_damage(damage)