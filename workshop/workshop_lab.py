class InvalidColError(Exception):
    pass


class FullColumnError(Exception):
    pass


def print_matrix(ma):
    """The function print the matrix when needed"""
    for element in ma:
        print(element)


def validate_col_choice(selected_column_num, max_column_index):
    if not 0 <= selected_column_num <= max_column_index:
        raise InvalidColError


def place_player_choice(ma, selected_col_index, player_num):
    rows = len(ma)
    for row_idx in range(rows_count-1, -1, -1):
        if ma[row_idx][selected_col_index] == 0:
            matrix[row_idx][selected_col_index] = player_num
            return row_idx, selected_col_index
    raise FullColumnError


def valid_player_spot(ma, row, col, player_num):
    if col <0 or row <0:
        return False
    try:
        if ma[row][col] == player_num:
            return True
    except IndexError:
        return False
    return False

rows_count = 6
cols_count = 7
matrix = [[0 for j in range(cols_count)] for i in range(rows_count)]
print_matrix(matrix)

player_num = 1


def is_winner(ma, row, col, player_num, slots_count = 4 ):
    is_right = all([valid_player_spot(matrix, row, col+i, player_num) for i in range(slots_count)])
    is_left = all([valid_player_spot(matrix, row, col-i, player_num) for i in range(slots_count)])
    is_up = all([valid_player_spot(matrix, row-i, col, player_num) for i in range(slots_count)])
    is_down = all([valid_player_spot(matrix, row + i, col, player_num) for i in range(slots_count)])
    is_right_up = all([valid_player_spot(matrix, row - i, col+i, player_num) for i in range(slots_count)])
    is_left_up = all([valid_player_spot(matrix, row - i, col-i, player_num) for i in range(slots_count)])
    is_right_down = all([valid_player_spot(matrix, row + i, col+i, player_num) for i in range(slots_count)])
    is_left_down = all([valid_player_spot(matrix, row + i, col-i, player_num) for i in range(slots_count)])

    if any([is_right, is_left, is_up, is_down,is_right_up,is_left_up,  is_right_down, is_left_down ]):
        return True
    return False

while True:
    player_num = 2 if player_num % 2 == 0 else 1 #define the player numbers

    #TODO: Read column choice from input:
    try:
        col_num = int(input(f"Player {player_num}, please choose a column from 1 to 7: ")) - 1
        # -1 added because we need to use the indeces
        validate_col_choice(col_num, cols_count)
        row, col = place_player_choice(matrix, col_num, player_num)
        if is_winner(matrix, row, col, player_num):
            print(f"The winner is player {player_num}")
            print(matrix)
            break
        print_matrix(matrix)

    except InvalidColError:
        print(f"This column is not in range. Please, try another digit from 1 to {cols_count} (inclusive). ")
        continue
    except ValueError:
        print("Please, select a valid digit!")
        continue
    except FullColumnError:
        print(f"Player {player_num}, the top of the board has been reached. Chose another column number please.")
        continue
    player_num += 1
