def check_if_is_outside(size, r, c):
    if r < 0:
        return size - 1, c
    elif c < 0:
        return r, size - 1
    elif r >= size:
        return 0, c
    elif c >= size:
        return r, 0
    else:
        return r, c


def get_next_pos(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


size = int(input())
matrix = []
current_row = None
current_col = None
total_coins = 0
directions = ['up', 'down', 'left', 'right']
is_winner = False
path = []


for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == "P":
            current_row, current_col = row, col
            path.append([current_row, current_col])
while True:
    if total_coins >= 100:
        is_winner = True
        break

    direction = input()

    if direction not in directions:
        continue

    current_row, current_col = get_next_pos(direction, current_row, current_col)
    current_row, current_col = check_if_is_outside(size, current_row, current_col)
    current_value = matrix[current_row][current_col]
    path.append([current_row, current_col])


    if current_value != 'P' and current_value != 'X':
        total_coins += int(current_value)
        matrix[current_row][current_col] = 0

    elif current_value == 'X':
        total_coins = total_coins // 2
        break

if is_winner:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {total_coins} coins.")
print(f"Your path:")
for coordinates in path:
    print(coordinates)