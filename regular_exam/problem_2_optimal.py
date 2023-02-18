def calculate_position_is_outside(next_row, next_col, rows, cols):
    return next_row<0 or next_row>=rows or next_col<0 or next_col>=cols


rows, cols = [int(x) for x in input().split()]

playground_mtrx = []
touched_oponents = 0
moves = 0
player_row, player_col = 0, 0
players_to_be_touched = 0

for row in range(rows):
    row_elements = input().split()
    playground_mtrx.append(row_elements)

    for col in range(cols):
        if row_elements[col] == "B":
            player_row = row
            player_col = col

        if row_elements[col] == "P":
            players_to_be_touched += 1

directions_mapper = {
    'up': lambda x, y: [x - 1, y],
    'down': lambda x, y: [x + 1, y],
    'left': lambda x, y: [x, y - 1],
    'right': lambda x, y: [x, y + 1]
}

is_game_over = False
direction = input()

while direction != "Finish":
    next_row, next_col = directions_mapper[direction](player_row, player_col)

    if calculate_position_is_outside(next_row, next_col, rows, cols) or playground_mtrx[next_row][next_col] == "O":
        direction = input()
        continue

    player_row, player_col = next_row, next_col
    moves += 1

    if playground_mtrx[player_row][player_col] == "P":
        players_to_be_touched -= 1
        touched_oponents += 1

        if players_to_be_touched == 0:
            is_game_over = True
            player_row, player_col = next_row, next_col
            break

    direction = input()

print("Game over!")
print(f"Touched opponents: {touched_oponents} Moves made: {moves}")
