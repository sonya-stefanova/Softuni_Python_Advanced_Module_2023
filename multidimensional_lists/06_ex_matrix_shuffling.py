def id_out_of_index(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input()
    if command == 'END':
        break

    # swap 0 0 1 1
    command_args = command.split()

    if len(command_args) != 5 or command_args[0] != 'swap':
        print('Invalid input!')
        continue

    row1, col1, row2, col2 = [int(x) for x in command_args[1:]]

    if id_out_of_index(row1, col1, rows, cols) or id_out_of_index(row2, col2, rows, cols):
        print('Invalid input!')
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(*row, sep=' ')