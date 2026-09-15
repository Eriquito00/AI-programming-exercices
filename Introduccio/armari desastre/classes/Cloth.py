import random as rd

class Cloth:
    TYPE = ["PANTALONS", "SAMARRETES", "JERSEY", "PANTALO CURT", "ROBA INTERIOR"]
    COLOR = ["BLAU", "GRIS", "NEGRE"]

    def __init__(self):
        self.type = self.TYPE[rd.randint(0, len(self.TYPE) - 1)]
        self.color = self.COLOR[rd.randint(0, len(self.COLOR) - 1)]
        self.price = self.generate_price()

    def generate_price(self) -> int:
        match self.type:
            case "PANTALONS": return rd.randint(25, 75)
            case "SAMARRETES": return rd.randint(10, 25)
            case "JERSEY": return rd.randint(20, 45)
            case "PANTALO CURT": return rd.randint(15, 55)
            case "ROBA INTERIOR": return rd.randint(5, 15)
        return 0

    def toString(self) -> str:
        return f"{self.type} de color {self.color} de preu {self.price}€"