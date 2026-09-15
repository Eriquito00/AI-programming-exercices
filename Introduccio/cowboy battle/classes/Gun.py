class Gun:
    MAX_BULLETS = 3
    def __init__(self, bullets: int):
        self.bullets = bullets

    def recharge(self) -> None:
        if self.bullets < Gun.MAX_BULLETS:
            self.bullets += 1

    def shoot(self) -> bool:
        if self.bullets > 0:
            self.bullets -= 1
            return True
        else:
            return False