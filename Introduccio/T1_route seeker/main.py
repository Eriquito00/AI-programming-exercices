MOVEMENTS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

MATRIX = [
    ["x",     "x", "x", "x", "x", "GOAL"],
    ["R",     "R", "R", "x", "x", "R"],
    ["R",     "x", "R", "x", "x", "R"],
    ["R",     "x", "R", "R", "x", "R"],
    ["R",     "x", "x", "R", "x", "R"],
    ["START", "x", "x", "R", "R", "R"]
]           

#
def pot_moure(x: int, y: int, matrix_size: int, move_available: tuple[int, int], last_move: tuple[int, int]) -> bool:
    """Funcio que retorna True o False segons si es pot moure o no.

    Args:
        x (int): Posicio actual de fila
        y (int): Posicio actual de columna
        matrix_size (int): Longitud de la matriu
        move_available (tuple[int, int]): Tupla amb el moviment que volem mirar si es pot o no fer
        last_move (tuple[int, int]): Tupla amb l'ultim moviment que s'ha fet
    Tant move_available com last_move son adalt, abaix, esquerra, dreta no coordenada de l'anterior moviment

    Returns:
        bool: True si es pot moure, False si no es pot moure
    """
    moviment_x, moviment_y = move_available
    seguent_x = x + moviment_x
    seguent_y = y + moviment_y

    if not (0 <= seguent_x < matrix_size and 0 <= seguent_y < matrix_size):
        return False

    if last_move and move_available == (-last_move[0], -last_move[1]):
        return False

    return True

def search_value(matrix: list[list[str]], searching_for: str) -> tuple[int, int]:
    """Funcio creada per Trobar la primera posicio d'un string especific a la matriu

    Args:
        matrix (list[list[str]]): Matriu on es vol buscar el string
        searching_for (str): String que es vol trobar

    Returns:
        tuple[int, int]: Tupla amb la coordenada de la primera aparicio del string
    """
    for fila, row in enumerate(matrix):
        for columna, valor in enumerate(row):
            if valor == searching_for:
                return (fila, columna)
    return None

def main(matrix: list[list[str]]):
    matrix_size: int = len(matrix)
    position = search_value(matrix, "START")
    end = search_value(matrix, "GOAL")

    route = [position]
    last_position = []

    while position != end:
        # Comprovar per cadascun dels 4 moviments si es poden fer
        for move_available in MOVEMENTS:
            if pot_moure(
                position[0],
                position[1],
                matrix_size,
                move_available,
                last_position,
            ):
                # Guardem les coordenades del moviment que volem fer
                next = (
                    position[0] + move_available[0],
                    position[1] + move_available[1],
                )

                # Si el moviment no esta a la ruta (per no tornar enrere)
                # I si el moviment es pot fer (es una "R" o el "GOAL")
                if (
                    next not in route
                    and 
                    matrix[next[0]][next[1]] in ("R", "GOAL")
                ):
                    # Afegim a la llista la coordenada, ens posem a la coordenada y posem com ultim moviment el moviment que hem fet
                    route.append(next)
                    position = next
                    last_position = move_available
                    break
        else:
            # Si no es pot fer cap moviment no es pot arribar
            raise ValueError("No existeix cap ruta fins a l'objectiu")

    # Una vegada arribem al "GOAL" estilitzem la ruta y la treiem per consola
    route_format = " > ".join(
        f"({fila + 1}, {columna + 1})" for fila, columna in route
    )
    print(f"El camí per poder arribar a l'objectiu es: {route_format}")

main(MATRIX)