def move_rover(direction, row, col):
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def reposition_rover(row, col, size):
    if row < 0:
        return size - 1, col
    if row >= size:
        return 0, col
    if col < 0:
        return row, size - 1
    if col >= size:
        return row, 0


current_row, current_col = 0, 0

size = 6
matrix = []

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(size):
        if row_elements[col] == 'E':
            current_row, current_col = row, col

directions = input().split(", ")

water_found = False
metal_found = False
concrete_found = False

for direction in directions:
    current_row, current_col = move_rover(direction, current_row, current_col)

    if is_outside(current_row, current_col, size):
        current_row, current_col = reposition_rover(current_row, current_col, size)

    value = matrix[current_row][current_col]
    if value == 'W':
        water_found = True
        print(f'Water deposit found at ({current_row}, {current_col})')
    elif value == 'M':
        metal_found = True
        print(f'Metal deposit found at ({current_row}, {current_col})')
    elif value == 'C':
        concrete_found = True
        print(f'Concrete deposit found at ({current_row}, {current_col})')
    elif value == 'R':
        print(f'Rover got broken at ({current_row}, {current_col})')
        break

if water_found and metal_found and concrete_found:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')