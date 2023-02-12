# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0

def find_valid_knights_count(row, col, chess_board):
    #find the possible coordinates a knight can do:
    possible_attacks = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1]
    ]

    #check how many valid knights can be attacked if the next step of the knight attackes a K:
    #count how many of them are valid attacks
    counter = 0
    for r, c in possible_attacks:
        if 0 <= r < len(chess_board) and 0 <= c < len(chess_board) and chess_board[r][c] == 'K':
            counter += 1
    return counter

size = int(input())
chess_board = [list(input()) for _ in range(size)]

removed_knights = 0

while True:
    best_count = 0
    knight_row, knight_col = 0, 0

#traverse the matrix from the beginning:
    for row in range(size):
        for col in range(size):

            #if current cell is empty, skip it and continue until a knight is found.
            if chess_board[row][col] == '0':
                continue

            #else: find how many knighst can be attacked.
            count = find_valid_knights_count(row, col, chess_board)
            if count > best_count:
                best_count = count
                knight_row = row
                knight_col = col
    if best_count == 0:
        break

    #empty the knight's cell:
    chess_board[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)