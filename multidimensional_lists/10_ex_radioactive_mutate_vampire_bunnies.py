def get_next_pos(row, col, command):
    if command == 'U':
        return row - 1, col
    if command == 'D':
        return row + 1, col
    if command == 'L':
        return row, col - 1
    if command == 'R':
        return row, col + 1


def outside_border_reached(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


def get_children(row, col, rows, cols):
    possible_children = [
        [row - 1, col],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col]
    ]

    result = []
    for child_row, child_col in possible_children:
        if not outside_border_reached(child_row, child_col, rows, cols):
            result.append([child_row, child_col])

    return result


rows, cols = [int(x) for x in input().split()]

bunnies = set()
p_row = 0
p_col = 0

matrix = []

for row in range(rows):
    row_elements = list(input())

    for col in range(cols):
        if row_elements[col] == 'P':
            p_row, p_col = row, col
        elif row_elements[col] == 'B':
            bunnies.add(f'{row} {col}')
    matrix.append(row_elements)

commands = input()

won = False
dead = False

for command in commands:
    next_row, next_col = get_next_pos(p_row, p_col, command)
    matrix[p_row][p_col] = '.'

    if outside_border_reached(next_row, next_col, rows, cols):
        won = True
    elif matrix[next_row][next_col] == 'B':
        dead = True
        p_row, p_col = next_row, next_col
    else:
        matrix[next_row][next_col] = 'P'
        p_row, p_col = next_row, next_col

    new_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]
        children = get_children(bunny_row, bunny_col, rows, cols)
        for child_row, child_col in children:
            new_bunnies.add(f'{child_row} {child_col}')
            matrix[child_row][child_col] = 'B'
            if child_row == p_row and child_col == p_col:
                dead = True

    bunnies = bunnies.union(new_bunnies)

    if won or dead:
        break

for row in matrix:
    print(''.join(row))

if won:
    print(f'won: {p_row} {p_col}')
else:
    print(f'dead: {p_row} {p_col}')