from classes.Armari import Armari

def show_menu() -> int:
    print("Benvingut a l'armari de roba!")
    print("1. Consulta armari")
    print("2. Cuantitat de cada roba")
    print("3. Cuantitat de roba per color")
    print("4. Preu total de l'armari")
    print("5. Regenera armari")
    print("6. Sortir")

    i = int(input("Selecciona una opció: "))
    while i < 1 or i > 6:
        i = int(input("Selecciona una opció: "))

    return i

armari = Armari(50)
while True:
    option = show_menu()
    match option:
        case 1:
            print(armari.show_armari())
        case 2:
            print(armari.count_cloths())
        case 3:
            print(armari.count_cloths_by_color())
        case 4:
            print(armari.total_price())
        case 5:
            armari = Armari(50)
            print("Armari regenerat!")
        case 6:
            print("Sortint...")
            exit()