def outside_dashboard(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size

def calc_total(dashboard, row, col, size):
    element = dashboard[row][col]
    if element.isdigit():
        total_scores_mapper[current_player] -= int(element)

    elif element == "D":
        total_scores_mapper[current_player] -= 2*(int(dashboard[row][0]) + int(dashboard[row][6]) + int(dashboard[0][col]) + int(dashboard[6][col]))


    elif element == "T":
        total_scores_mapper[current_player] -= 3 * \
                    (int(dashboard[row][0]) + \
                    int(dashboard[row][6]) + \
                    int(dashboard[0][col]) + \
                    int(dashboard[6][col]))

    return total_scores_mapper


size = 7
first_player, second_player = input().split(", ")

dashboard = [input().split() for x in range(size)]

total_scores_mapper = {
    first_player: 501,
    second_player: 501
}

game_win = False

turn = 1
throw = 0
winner = ''

while True:
    current_player = first_player if turn % 2 != 0 else second_player
    throw += 1
    row, col = eval(input())

    if outside_dashboard(row, col, size):
        continue
    elif dashboard[row][col] == "B":
        game_win = True
        winner = current_player
        break
    else:
        calc_total(dashboard, row, col, size)

    if total_scores_mapper[current_player] <= 0:
        game_win = True
        winner = current_player
    turn += 1

if game_win:
    print(f"{winner} won the game with {throw} throws!")



