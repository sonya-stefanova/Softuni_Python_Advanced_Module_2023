# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0

def find_count(row, col, chess_board):
    possible_moves = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1]
    ]

    counter = 0
    for r, c in possible_moves:
        if 0 <= r < len(chess_board) and 0 <= c < len(chess_board) and chess_board[r][c] == 'K':
            counter += 1
    return counter

size = int(input())

chess_board = []

for row in range(size):
    chess_board.append(list(input()))

removed_knights = 0

while True:
    best_count = 0
    knight_row = 0
    knight_col = 0

    for row in range(size):
        for col in range(size):

            if chess_board[row][col] == '0':
                continue

            count = find_count(row, col, chess_board)
            if count > best_count:
                best_count = count
                knight_row = row
                knight_col = col
    if best_count == 0:
        break

    chess_board[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)