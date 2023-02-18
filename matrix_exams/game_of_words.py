def get_next_pos(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


initial_string = input()
size = int(input())

matrix = []

current_row = None
current_col = None


for row in range(size):
    row_elements = list(input())
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == "P":
            current_row = row
            current_col = col

number = int(input())

for _ in range(number):
    command = input()

    next_pos_row, next_pos_col = get_next_pos(command, current_row, current_col)

    if is_inside(next_pos_row, next_pos_col, size):
        if matrix[next_pos_row][next_pos_col] == "-":
            pass
        else:
            collected_letter = matrix[next_pos_row][next_pos_col]
            initial_string += collected_letter
        matrix[next_pos_row][next_pos_col] = 'P'
        matrix[current_row][current_col] = '-'
        current_row, current_col = next_pos_row, next_pos_col
    else:
        if initial_string:
            initial_string = initial_string[:-1]

print(f"{initial_string}")
for row in matrix:
    print(*row, sep='')