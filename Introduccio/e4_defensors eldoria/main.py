import random as rd

from classes.Character import Character
from classes.Barbarian import Barbarian
from classes.Sorcerer import Sorcerer
from classes.Palladium import Palladium
from classes.Enemy import Enemy

oleguer = Barbarian("Oleguer", 1, 135, 26)
david = Palladium("David", 1, 110, 18, 12)
sergi = Sorcerer("Sergi", 1, 80, 40)

heroes: list[Character] = [oleguer, david, sergi]
enemy = Enemy("Black Knight", 250)

turn = 1

while enemy.is_alive() and any(h.is_alive() for h in heroes):
    for h in heroes:
        if h.is_alive() and enemy.is_alive():
            h.action(enemy)

    if enemy.is_alive():
        alive_heroes = [h for h in heroes if h.is_alive()]

        if alive_heroes:
            objective = rd.choice(alive_heroes)
            enemy.phisical_attack(objective)

    print("\n[Estat després del torn]")
    enemy.info()
    for heroi in heroes:
        heroi.info()

    turn += 1

print("\n==========================")
if enemy.is_alive():
    print("❌ DERROTA: Tots els herois han caigut!")
else:
    print("✅ VICTÒRIA: L'enemic ha estat derrotat!")
print("==========================")