
crud_matrix = [[x for x in input().split()] for _ in range(6)]
row, column = eval(input())
size = 6

def is_in_matrix(curr_row, curr_col, size):
    return 0 <= curr_row < size and 0 <= curr_col < size

directions = {
    'up': lambda row, col: (row - 1, col),
    'down': lambda row, col: (row + 1, col),
    'right': lambda row, col: (row, col + 1),
    'left': lambda row, col: (row, col - 1),
}
while True:
    line = input()
    if line == 'Stop':
        break

    line = line.split(', ')
    command, direction = line[0], line[1]
    next_row, next_col = directions[direction](row, column)

    if command == 'Create':
        value = line[2]
        if is_in_matrix(next_row, next_col, size):
            if crud_matrix[next_row][next_col] == '.':
                crud_matrix[next_row][next_col] = value
    elif command == 'Update':
        value = line[2]
        if is_in_matrix(next_row, next_col, size):
            if crud_matrix[next_row][next_col].isdigit() or crud_matrix[next_row][next_col].isalpha():
                crud_matrix[next_row][next_col] = value
    elif command == 'Delete':
        if is_in_matrix(next_row, next_col, size):
            if crud_matrix[next_row][next_col].isdigit() or crud_matrix[next_row][next_col].isalpha():
                crud_matrix[next_row][next_col] = '.'
    elif command == 'Read':
        if is_in_matrix(next_row, next_col, size):
            if crud_matrix[next_row][next_col].isdigit() or crud_matrix[next_row][next_col].isalpha():
                print(crud_matrix[next_row][next_col])

    row, column = next_row, next_col

[print(*row) for row in crud_matrix]