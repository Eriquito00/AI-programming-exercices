from classes.projectils.projectil import Projectil

class Tank:
    def __init__(self, name: str, faction: str, upper_armor: float, under_armor: float, loader: list[Projectil]):
        self.name = name
        self.faction = faction

        self.blindatge = [
            [upper_armor, upper_armor, upper_armor],
            [under_armor, under_armor, under_armor]
        ]
        self.loader = loader
        self.index_loader = 0

    # Si es True, el tanc està viu. Si és False, el tanc ha estat destruït.
    def esta_viu(self) -> bool:
        for i in self.blindatge:
            for j in i:
                if j < 0:
                    return False
        return True

    # Retorna el projectil que s'ha de disparar i actualitza l'index
    def seguent_projectil(self) -> Projectil:
        proj = self.loader[self.index_loader]
        self.index_loader = (self.index_loader + 1) % len(self.loader)
        return proj

    # Funcio que s'hereda a subclasses
    def rebre_impacte(self, dany_base: float) -> tuple[str, float]:
        return "impacte", dany_base

    # Aplica dany a la posicio del blindatge especific
    def aplicar_dany(self, dany: float, fila: int, col: int):
        self.blindatge[fila][col] = round(self.blindatge[fila][col] - dany, 2)

    def __str__(self):
        return f"{self.name} ({self.faction}) - Blindatge: {self.blindatge}"