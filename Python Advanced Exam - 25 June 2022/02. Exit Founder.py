first_player, second_player = input().split(", ")
size = 6
matrix = [input().split() for x in range(size)]

resting_players = []
game_over = False
is_resting = False
row, col = 0, 0

turn = 1
while not game_over:
    current_player = first_player if turn % 2 != 0 else second_player
    row, col = [int(x) for x in input() if x.isdigit()]

    if current_player in resting_players:
        resting_players.remove(current_player)
        turn+=1
        continue

    if matrix[row][col] == ".":
        turn+=1
        continue

    elif matrix[row][col] == "W":
        print(f'{current_player} hits a wall and needs to rest.')
        is_resting = True
        resting_players.append(current_player)
        turn+=1
        continue

    elif matrix[row][col] == "E":
        game_over = True
        print(f"{current_player} found the Exit and wins the game!" )
        break

    elif matrix[row][col]=="T":
        game_over = True
        winner = second_player if current_player == first_player else first_player
        print(f"{current_player} is out of the game! The winner is {winner}.")
        break

    turn+=1