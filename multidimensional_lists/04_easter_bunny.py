import sys

def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def move_up(row, col):
    return row-1, col

def move_down(row, col):
    return(row+1, col)


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


size = int(input())
matrix = []
bunny_row, bunny_col = 0,0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == "B":
            bunny_row, bunny_col = row, col

directions = {
    'up': move_up,
    'down': move_down,
    'left': move_left,
    'right': move_right
}


best_score = -sys.maxsize
best_direction = ''
best_path = []

for direction, next_step in directions.items():
    current_row, current_col = bunny_row, bunny_col
    current_score = 0
    current_path = []

    while True:
        current_row, current_col = next_step(current_row, current_col)

        if is_outside(current_row, current_col, size):
            break

        if matrix[current_row][current_col] == 'X':
            break

        current_score += int(matrix[current_row][current_col])
        current_path.append([current_row, current_col])

        if current_score > best_score and current_path:
            best_score = current_score
            best_direction = direction
            best_path = current_path
print(best_direction)
print(*best_path, sep='\n')
print(best_score)