first_player, second_player = input().split(", ")
players = [first_player, second_player]
SIZE = 6
maze_board = []
traps = []
walls = []
curr_player_row, curr_player_col = None, None


for row in range(SIZE):
    row_elements = input().split()
    maze_board.append(row_elements)
    for col in range(SIZE):
        if row_elements[col] == "T":
            traps.append([row,col])
        if row_elements[col] == "W":
            walls.append([row, col])

resting_players = []
turn = 0
coords = input()
while coords:
    current_player = first_player if turn % 2 == 0 else second_player
    coords = [int(x) for x in coords if x.isdigit()]
    current_player_row, curr_player_col = coords

    if current_player in resting_players:
        turn+=1
        coords = input()
        continue

    if maze_board[current_player_row][curr_player_col] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif maze_board[current_player_row][curr_player_col] in traps:
        players.remove(current_player)
        print(f"{current_player} is out of the game! The winner is {players[0]}.")
        break
    elif maze_board[current_player_row][curr_player_col] in walls:
        print(f"{current_player} hits a wall and needs to rest.")
        resting_players.append(current_player)
        continue

    turn+=1
    coords = input()

