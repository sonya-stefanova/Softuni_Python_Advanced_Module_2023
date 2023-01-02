# 5 6
# .....P
# ......
# ...B..
# ......
# ......
# ULDDDR


def get_next_position(command, row, col):
    if command == 'U':
        return row - 1, col
    if command == 'D':
        return row + 1, col
    if command == 'L':
        return row, col - 1
    if command == 'R':
        return row, col + 1


def invalid(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(x) for x in input().split()]
matrix = []
player_row = 0
player_col = 0

bunnies = set()

for row in range(rows):
    row_elements = list(input())
    matrix.append(row_elements)

    for col in range(cols):
        element = row_elements[col]
        if element == "P":
            player_row = row
            player_col = col
        elif element == "B":
            bunnies.add(f'{row} {col}')

commands = input()
# ULDDDR.
matrix[player_row][player_col] = "."
won = False
is_dead = False

for command in commands:
    next_row, next_col = get_next_position(command, player_row, player_col)

    if invalid(next_row, next_col, rows, cols):
        won = True
    elif matrix[next_row][next_col] == "B":
        is_dead = True
        player_row, player_col = next_row, next_col
    else:
        player_row, player_col = next_row, next_col

    new_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]

        if not invalid(bunny_row - 1, bunny_col, rows, cols):
            new_bunnies.add(f'{bunny_row - 1} {bunny_col}')
            matrix[bunny_row-1][bunny_col] = "B"

        if not invalid(bunny_row + 1, bunny_col, rows, col):
            new_bunnies.add(f'{bunny_row + 1} {bunny_col}')
            matrix[bunny_row+1][bunny_col] = "B"

        if not invalid(bunny_row, bunny_col - 1, rows, col):
            new_bunnies.add(f'{bunny_row} {bunny_col - 1}')
            matrix[bunny_row][bunny_col-1] = "B"

        if not invalid(bunny_row, bunny_col + 1, rows, col):
            new_bunnies.add(f'{bunny_row} {bunny_col + 1}')
            matrix[bunny_row][bunny_col+1] = "B"

    bunnies = bunnies.union(new_bunnies)

    if matrix[player_row][player_col] == "B":
        is_dead = True

    if won or is_dead:
        break

for row in matrix:
    print(*row, sep = "")

if won:
    print(f'won: {player_row} {player_col}')
else:
    print(f'dead: {player_row} {player_col}')
