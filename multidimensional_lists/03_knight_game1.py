# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0

def is_knight(row, col, matrix):
    return matrix[row][col] == "K"

def is_inside(row, col, matrix):
    return 0<=row<len(matrix) and 0<=col<len(matrix)

def find_count(row, col, matrix):
    result = 0

    if is_inside(row-2, col-1, len(matrix)) and is_knight(row-2, col-1, matrix):
        result+=1
    if is_inside(row - 2, col + 1, len(matrix)) and is_knight(row - 2, col + 1, matrix):
        result+=1
    if is_inside(row - 1, col - 2, len(matrix)) and is_knight(row - 1, col - 2, matrix):
        result+=1
    if is_inside(row - 1, col + 2, len(matrix)) and is_knight(row - 1, col + 2, matrix):
        result+=1
    if is_inside(row + 1, col - 2, len(matrix)) and is_knight(row + 1, col - 2, matrix):
        result+=1
    if is_inside(row + 1, col + 2, len(matrix)) and is_knight(row + 1, col + 2, matrix):
        result+=1
    if is_inside(row + 2, col - 1, len(matrix)) and is_knight(row + 2, col - 1, matrix):
        result+=1
    if is_inside(row + 2, col + 1, len(matrix)) and is_knight(row + 2, col + 1, len(matrix)):
        result+=1
    return result


    counter = 0
    for r, c in possible_moves:
        if 0 <= r < len(chess_board) and 0 <= c < len(chess_board) and chess_board[r][c] == 'K':
            counter += 1
    return counter

size = int(input())

matrix = []

for row in range(size):
    matrix.append(list(input()))

removed_knights = 0

while True:

    table = {}

    best_count = 0
    knight_row = 0
    knight_col = 0

    for row in range(size):
        for col in range(size):

            if matrix[row][col] == '0':
                continue

            count = find_count(row, col, matrix)
            table[(row, col)] = count

    if len(table) == 0:
        break

    best_counter = 0
    knight_row, knight_col = 0, 0
    for coords, counter in table.items():

        if counter > best_counter:
            best_counter = counter
            knight_row = coords[0]
            knight_col = coords[1]

    matrix[knight_row][knight_col] = "0"
    removed_knights+=1
print(removed_knights)