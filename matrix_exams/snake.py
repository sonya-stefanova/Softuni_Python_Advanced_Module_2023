def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size

size = int(input())
matrix = []
snake_row, snake_col = 0, 0
burrow_coords = []

directions_mapper = {
    'up': lambda x, y: [x - 1, y],
    'down':lambda x, y: [x + 1, y],
    'left':lambda x, y: [x, y - 1],
    'right': lambda x, y: [x, y + 1]
}

for row in range(size):
    row_elements = list(input())
    matrix.append(row_elements)
    for col in range(size):
        if row_elements[col] == "S":
            snake_row, snake_col = row, col
        if row_elements[col] == "B":
            burrow_coords.append([row, col])

REQUIRED_FOOD = 10
food_eaten = 0
matrix[snake_row][snake_col] = "."

while True:
    direction = input()
    matrix[snake_row][snake_col] = "."
    snake_row, snake_col = directions_mapper[direction](snake_row, snake_col)

    if not is_valid(snake_row, snake_col, size):
        print("Game over!")
        break

    if  matrix[snake_row][snake_col] == "*":
        REQUIRED_FOOD-=1
        food_eaten +=1
        matrix[snake_row][snake_col] = "."
        if REQUIRED_FOOD==0:
            print(f"You won! You fed the snake.")
            matrix[snake_row][snake_col] = "S"

            break

    elif matrix[snake_row][snake_col] == "B":
        matrix[snake_row][snake_col] = "."
        for coord in burrow_coords:
            if [snake_row, snake_col] in burrow_coords:
                burrow_coords.remove([snake_row, snake_col])
        snake_row, snake_col = burrow_coords[0]


    elif matrix[snake_row][snake_col] == "-":
        matrix[snake_row][snake_col] = "."


    matrix[snake_row][snake_col] = "S"

print(f'Food eaten: {food_eaten}')
[print(*row, sep = '') for row in matrix]