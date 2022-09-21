#!/usr/bin/env python3
# Ejercicio 1

# Tienes un tablero de 7 x 7 en el cual se encuentra solo un posible camino para que tu el principe salves a la princesa,
# pero solo puedes cruzar por el camino que se encuentra marcado por las 'O', las casillas marcadas por 'X' son barricadas,
# tu mision es encontrar el camino mas corto para encontrar a tu princesa.
#
# o.o  ----------------------------
#      | O | O | O | O | O | X | X |
#      ----------------------------
#      | X | O | X | O | O | X | X |
#      ----------------------------
#      | O | O | X | X | O | X | X |
#      ----------------------------
#      | O | O | O | X | O | X | X |
#      ----------------------------
#      | X | X | O | X | O | O | O |
#      ----------------------------
#      | X | X | O | X | O | X | O |
#      ----------------------------
#      | X | X | O | O | O | X | O |  O.O
#      ----------------------------

board = [['O', 'O', 'O', 'O', 'O', 'X', 'X'],
         ['X', 'O', 'X', 'O', 'O', 'X', 'X'],
         ['O', 'O', 'X', 'X', 'O', 'X', 'X'],
         ['O', 'O', 'O', 'X', 'O', 'X', 'X'],
         ['X', 'X', 'O', 'X', 'O', 'O', 'O'],
         ['X', 'X', 'O', 'X', 'O', 'X', 'O'],
         ['X', 'X', 'O', 'O', 'O', 'X', 'O']]


# Get all the 'O' indexes
o_paths = []
for x, row in enumerate(board):
    for y, cell in enumerate(row):
        if cell == 'O':
            o_paths.append((x + 1, y + 1))

# Choose the right path from the goal to the beginning as always the indexes
# are going to be lower
shortest_path = []
for cell_coordinates in sorted(o_paths, reverse=True):
    x = cell_coordinates[0]
    y = cell_coordinates[1]

    if len(shortest_path) == 0:
        shortest_path.append(cell_coordinates)
    elif x == shortest_path[-1][0]:
        if y == shortest_path[-1][1] - 1:
            shortest_path.append(cell_coordinates)
    elif y == shortest_path[-1][1]:
        if x == shortest_path[-1][0] - 1:
            shortest_path.append(cell_coordinates)

print(shortest_path)

