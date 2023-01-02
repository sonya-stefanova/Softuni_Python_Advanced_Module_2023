def move_snake(r, c, direction):

    if direction == "up":
        r -= 1
    elif direction == "down":
        r += 1
    elif direction == "left":
        c -= 1
    elif direction == "right":
        c += 1

    return r, c

size = int(input())
matrix = []
snake_row = 0
snake_col = 0
lair_burrows = []
food_quantity = 0
snake_out = False
is_enough_food = False

for row in range(size):
    row_elements = list(input())
    matrix.append(row_elements)
    for col in range(size):
        if row_elements[col] == "S":
            snake_row = row
            snake_col = col
        if row_elements[col] == "B":
            burrow_row = row
            burrow_col = col
            lair_burrows.append((burrow_row, burrow_col))

while True:
    direction = input()
    matrix[snake_row][snake_col] = "."
    snake_row, snake_col = move_snake(snake_row, snake_col, direction)

    if snake_row < 0 or snake_row >=size or snake_col < 0 or snake_col >= size:
        snake_out = True
        break

    if matrix[snake_row][snake_col] == "*":
        food_quantity += 1
    elif matrix[snake_row][snake_col] == ".":
        pass
    elif matrix[snake_row][snake_col] == "B":
        matrix[snake_row][snake_col] = "."
        lair_burrows.remove((snake_row, snake_col))
        snake_row, snake_col = lair_burrows[0]

    matrix[snake_row][snake_col] = "S"

    if food_quantity >= 10:
        is_enough_food = True
        break

if snake_out:
    print("Game over!")

if is_enough_food:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_quantity}")

for row in matrix:
    print(*row, sep="")