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

def pot_moure(x: int, y: int, matrix_size: int, move_available: tuple[int, int], last_move: tuple[int, int]) -> bool:
    moviment_x, moviment_y = move_available
    seguent_x = x + moviment_x
    seguent_y = y + moviment_y

    if not (0 <= seguent_x < matrix_size and 0 <= seguent_y < matrix_size):
        return False

    if last_move and move_available == (-last_move[0], -last_move[1]):
        return False

    return True

def search_value(matrix: list[list[str]], searching_for: str) -> tuple[int, int]:
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
        for move_available in MOVEMENTS:
            if pot_moure(
                position[0],
                position[1],
                matrix_size,
                move_available,
                last_position,
            ):
                next = (
                    position[0] + move_available[0],
                    position[1] + move_available[1],
                )

                if (
                    next not in route
                    and 
                    matrix[next[0]][next[1]] in ("R", "GOAL")
                ):
                    route.append(next)
                    position = next
                    last_position = move_available
                    break
        else:
            raise ValueError("No existeix cap ruta fins a l'objectiu")

    route_format = " > ".join(
        f"({fila + 1}, {columna + 1})" for fila, columna in route
    )
    print(f"El camí per poder arribar a l'objectiu es: {route_format}")

main(MATRIX)