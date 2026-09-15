from classes.Gun import Gun
class Cowboy:
    def __init__(self, name: str, health: int, gun: Gun):
        self.name = name
        self.health = health
        self.gun = gun

    def is_alive(self) -> bool:
        return self.health > 0

    def shoot(self) -> bool:
        if self.gun.shoot():
            return True
        else:
            self.gun.recharge()
            return False

    def get_shoot(self) -> int:
        self.health -= 1
        return self.health

    def recharge(self) -> None:
        self.gun.recharge()

    def toString(self) -> str:
        return f"Cowboy: {self.name}, Health: {self.health}, Gun: {self.gun.bullets} bullets"