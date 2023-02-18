def get_next_pos(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def is_outside(rows, cols, my_pos_row, my_pos_col):
    if my_pos_row < 0:
        return rows - 1, my_pos_col
    elif my_pos_col < 0:
        return my_pos_row, cols - 1
    elif my_pos_row > rows - 1:
        return 0, my_pos_col
    elif my_pos_col > cols - 1:
        return my_pos_row, 0
    else:
        return my_pos_row, my_pos_col


def items_collection_in_dictionary(matrix, my_pos_row, my_pos_col, gifts):
    if matrix[my_pos_row][my_pos_col] == "D":
        gifts['decorations'] += 1
    elif matrix[my_pos_row][my_pos_col] == "G":
        gifts['gifts'] += 1
    elif matrix[my_pos_row][my_pos_col] == "C":
        gifts['cookies'] += 1
    return gifts


rows, cols = [int(x) for x in input().split(', ')]

santa_matrix = []
curr_row, curr_col = 0, 0
total_items = 0
is_merry_christmas = False

collected_items = {
    'decorations': 0,
    'gifts': 0,
    'cookies': 0
    }

for row in range(rows):
    row_elements = input().split()
    santa_matrix.append(row_elements)

    for col in range(cols):
        if row_elements[col] == "Y":
            curr_row, curr_col = row, col

        if row_elements[col] != '.' and row_elements[col] != 'Y':
            total_items += 1

santa_matrix[curr_row][curr_col] = 'x'

command = input()

while command != 'End':

    direction = command.split('-')[0]
    steps = int(command.split('-')[1])

    for step in range(steps):
        curr_row, curr_col = get_next_pos(direction, curr_row, curr_col)
        if is_outside:
            curr_row, curr_col = is_outside(rows, cols, curr_row, curr_col)

            items_collection_in_dictionary(santa_matrix, curr_row, curr_col, collected_items)
            santa_matrix[curr_row][curr_col] = 'x'

            if sum(collected_items.values()) == total_items:
                santa_matrix[curr_row][curr_col] = 'Y'
                is_merry_christmas = True
                break

    if is_merry_christmas:
        break
    command = input()
    
santa_matrix[curr_row][curr_col] = 'Y'

if sum(collected_items.values()) == total_items:
    print("Merry Christmas!")
print(f"You've collected:")
print(f"- {collected_items.get('decorations')} Christmas decorations")
print(f"- {collected_items.get('gifts')} Gifts")
print(f"- {collected_items.get('cookies')} Cookies")

for row in santa_matrix:
    print(*row, sep=" ")