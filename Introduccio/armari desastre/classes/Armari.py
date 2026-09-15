from typing import List

from classes.Cloth import Cloth

class Armari:
    def __init__(self, num_cloths: int):
        self.armari: List[Cloth] = self.generate_armari(num_cloths)

    def generate_armari(self, num_cloths: int) -> List[Cloth]:
        armari: List[Cloth] = []
        for i in range(num_cloths):
            armari.append(Cloth())
        return armari

    def show_armari(self) -> str:
        str = ""
        for c in self.armari:
            str += c.toString() + "\n"
        return str

    def count_cloths(self) -> dict:
        count = {}
        for c in self.armari:
            if c.type in count:
                count[c.type] += 1
            else:
                count[c.type] = 1
        return count

    def count_cloths_by_color(self) -> dict:
        count = {}
        for c in self.armari:
            if c.color in count:
                count[c.color] += 1
            else:
                count[c.color] = 1
        return count

    def total_price(self) -> int:
        total = 0
        for c in self.armari:
            total += c.price
        return total