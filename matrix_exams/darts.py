def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size

def calc_points(player_row, player_col, darts, multiplier):
    total = (darts[player_row][0] + darts[player_row][6] + darts[0][player_col] + darts[6][player_col]) * multiplier
    return total


SIZE = 7
first_player, second_player = input().split(", ")

darts = [[int(x) if x.isdigit() else x for x in input().split()] for x in range(SIZE)]

first_player_turns, second_player_turns = 0, 0
starting_points = 501
current_points = starting_points
coords = input()

players = {
    first_player: {"points":501, "turn": 0},
    second_player: {"points":501, "turn": 0}
}
turn = 0
while coords:
    current_player = first_player if turn % 2 == 0 else second_player
    current_points = players[current_player]["points"]
    current_player_turns = players[current_player]["turn"]
    players[current_player]["turn"]+=1

    player_row, player_col = [int(x) for x in coords.lstrip("(").rstrip(")").split(", ")]

    if not is_valid(player_row, player_col, SIZE):
        continue

    if type(darts[player_row][player_col]) == int:
        current_points = darts[player_row][player_col]
        players[current_player]["points"]-=current_points
    elif darts[player_row][player_col] == "D":
        current_points = calc_points(player_row, player_col, darts, multiplier=2)
        players[current_player]["points"]-=current_points
    elif darts[player_row][player_col] == "T":
        current_points = calc_points(player_row, player_col, darts, multiplier=3)
        players[current_player]["points"]-=current_points

    elif darts[player_row][player_col] == "B":
        print(f"{current_player} won the game with {players[current_player]['turn']} throws!")
        break

    if players[current_player]["points"] <= 0:
        print(f"{current_player} won the game with {players[current_player]['turn']} throws!")
        break
    coords = input()
    turn += 1


