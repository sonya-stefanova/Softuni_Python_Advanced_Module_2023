battlefield_size = int(input())
matrix = []
submarine_row, submarine_col = 0, 0
cruisers_counter = 0

for row in range(battlefield_size):
    row_elements = list(input())
    matrix.append(row_elements)

    for col in range(battlefield_size):
        if row_elements[col] == "S":
            submarine_row, submarine_col = row, col
        cruisers_counter +=row_elements[col].count("C")

max_hits_counter = 3
mission_failed = False
last_row, last_col = None, None
battle_over_win = False
matrix[submarine_row][submarine_col] = "-"

directions = input()
directions_mapper = {
    'up': lambda x, y: [x - 1, y],
    'down':lambda x, y: [x + 1, y],
    'left':lambda x, y: [x, y - 1],
    'right': lambda x, y: [x, y + 1]
}

while directions:
    submarine_row, submarine_col = directions_mapper[directions](submarine_row, submarine_col)

    if matrix[submarine_row][submarine_col] == "-":
        directions = input()
        continue

    elif matrix[submarine_row][submarine_col] == "*":
        max_hits_counter-=1
        if max_hits_counter == 0:
            mission_failed = True
            last_row, last_col = submarine_row, submarine_col
            matrix[submarine_row][submarine_col] = "S"
            break

    elif matrix[submarine_row][submarine_col] == "C":
        cruisers_counter-=1
        if cruisers_counter == 0:
            battle_over_win = True
            matrix[submarine_row][submarine_col] = "S"
            break

    matrix[submarine_row][submarine_col] = "-"
    directions = input()


if mission_failed:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{last_row}, {last_col}]!")
elif battle_over_win:
    print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

for row in matrix:
    print(*row, sep = "")