# 5
# up right right up right
# * * * c *
# * * * e *
# * * c * *
# s * * c *
# * * c * *

def get_next_position(row, col, command):
    if command == "up":
        return row-1, col
    elif command == "down":
        return row + 1, col
    elif command == "right":
        return row, col+1
    elif command == "left":
        return row, col-1


size = int(input())
commands = input().split()
matrix = []

total_coals = 0
miner_row = 0
miner_col = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        element = row_elements[col]

        if element == "s":
            miner_row = row
            miner_col = col

        elif element == "c":
            total_coals += 1

game_over = False
for command in commands:
    next_row, next_col = get_next_position(miner_row, miner_col, command)
    if next_row<0 or next_row>=size or next_col<0 or next_col>=size:
        continue

    miner_row, miner_col = next_row, next_col

    if matrix[miner_row][miner_col] == "c":
        matrix[miner_row][miner_col] = "*"
        total_coals-=1
        if total_coals == 0:
            break
    elif matrix[miner_row][miner_col] == "e":
        game_over = True
        break

if total_coals == 0:
    print(f"You collected all coal! {miner_row, miner_col}")
elif game_over:
    print(f"Game over! {miner_row, miner_col}")
else:
    print(f"{total_coals} pieces of coal left. {miner_row, miner_col}")