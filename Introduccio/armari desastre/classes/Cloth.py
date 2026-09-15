import random as rd
from unittest import case

class Cloth:
    TYPE = ["PANTALONS", "SAMARRETES", "JERSEY", "PANTALO CURT", "ROBA INTERIOR"]
    COLOR = ["BLAU", "GRIS", "NEGRE"]

    def __init__(self):
        self.type = TYPE[rd.randint(0, len(self.type) - 1)]
        self.color = COLOR[rd.randint(0, len(self.color) - 1)]
        self.price = self.generate_price()

    def generate_price(self) -> int:
        match self.type:
            case "PANTALONS": return rd.randint(25, 75)
            case "SAMARRETES": return rd.randint(10, 25)
            case "JERSEY": return rd.randint(20, 45)
            case "PANTALO CURT": return rd.randint(15, 55)
            case "ROBA INTERIOR": return rd.randint(5, 15)

    def toString(self) -> str:
        return f"Cloth: {self.type}, Color: {self.color}, Price: {self.price}€"