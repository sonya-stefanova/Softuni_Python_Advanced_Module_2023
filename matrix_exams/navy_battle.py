def next_post_calc(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


battlefield_size = int(input())
matrix = []
submarine_row, submarine_col = 0, 0
cruisers_counter = 0

for row in range(battlefield_size):
    row_elements = list(input())
    matrix.append(row_elements)

    for col in range(battlefield_size):
        if "S" in row_elements[col]:
            submarine_row, submarine_col = row, col
        cruisers_counter +=row_elements[col].count("C")

max_hits_counter = 3
mission_failed = False
last_row, last_col = None, None
battle_over_win = False
matrix[submarine_row][submarine_col] = "-"

directions = input()
while directions:
    submarine_row, submarine_col = next_post_calc(directions, submarine_row, submarine_col)
    if not(0<=submarine_row<battlefield_size or 0<=submarine_col<battlefield_size):
        directions = input()
        continue

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