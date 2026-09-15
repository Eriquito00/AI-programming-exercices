from classes.Gun import Gun
from classes.Cowboy import Cowboy

def round_action(cb1: Cowboy, cb2: Cowboy) -> None:
    print(f"{cb1.name} quiere disparar a {cb2.name}")
    if (cb1.shoot()):
        print(f"DISPARA!!!")
        cb2.get_shoot()
    else:
        print(f"NO TIENE BALAS, RECARGA!!!")
        cb1.recharge()
    
    print(f"{cb1.name} tiene {cb1.health} vidas.")
    print(f"{cb2.name} tiene {cb2.health} vidas.")

def cowboy_decision() -> bool:
    print(f"¿Quieres disparar o recargar?")
    print(f"1) Disparar")
    print(f"2) Recargar")

    decision = input("Ingresa tu decisión (1 o 2): ")
    while decision not in ["1", "2"]:
        decision = input("Ingresa tu decisión (1 o 2): ")

    return decision == "1"

def cowboy_battle():
    cb1 = Cowboy("Eric", 5, Gun(1))
    cb2 = Cowboy("Oleguer", 5, Gun(1))
    round = 1

    while cb1.is_alive() and cb2.is_alive():
        print(f"Ronda {round}:")
        if round % 2 == 1:
            print(f"Turno de {cb1.name}")
            if cowboy_decision():
                round_action(cb1, cb2)
            else:
                cb1.recharge()
                print(f"{cb1.name} ha recargado su arma.")
        else:
            print(f"Turno de {cb2.name}")
            if cowboy_decision():
                round_action(cb2, cb1)
            else:
                cb2.recharge()
                print(f"{cb2.name} ha recargado su arma.")
        round += 1

    print("¡La batalla ha terminado!")
    if cb1.is_alive(): print(f"{cb1.name} ha ganado la batalla.")
    else: print(f"{cb2.name} ha ganado la batalla.")

cowboy_battle()