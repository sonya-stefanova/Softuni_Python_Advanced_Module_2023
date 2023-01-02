size = 7
darts = []
players = dict()

all_players = input().split(', ')
for each in all_players:
    players[each] = [501, 0]

darts = [input().split() for x in range(size)]


is_win = False
first_player, second_player = all_players

while True:
    command = input()[1:-1]
    row = int(command.split(", ")[0])
    col = int(command.split(", ")[1])

    if row < 0 or row >= 7 or col < 0 or col >= 7:
        pass

    else:
        target = darts[row][col]

        if target.isdigit():
            players[first_player][0] -= int(target)
        elif target == 'D':
            sum_points = 2 * (int(darts[row][0]) + int(darts[row][6]) + int(darts[0][col]) + int(darts[6][col]))
            players[first_player][0] -= sum_points
        elif target == 'T':
            sum_points = 3 * (int(darts[row][0]) + int(darts[row][6]) + int(darts[0][col]) + int(darts[6][col]))
            players[first_player][0] -= sum_points
        elif target == 'B':
            is_win = True

    players[first_player][1] += 1
    if is_win or players[first_player][0] <= 0:
        break
    first_player, second_player = second_player, first_player

print(f'{first_player} won the game with {players[first_player][1]} throws!')