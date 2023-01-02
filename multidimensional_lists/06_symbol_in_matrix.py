rows = int(input())

matrix = []
for _ in range(rows):
    line = list(input())
    matrix.append(line)

searched_symbol = input()
position = None
for row_index in range(rows):
    for col_index in range(rows):
        if searched_symbol == matrix[row_index][col_index]:
            position =(row_index, col_index)
            print(position)
            break
    if position:
        break
if not position:
    print(f"{searched_symbol} does not occur in the matrix")


rows = int(input())

matrix = []
for _ in range(rows):
    line = list(input())
    matrix.append(line)

searched_symbol = input()
position = None
for row_index in range(rows):
    for col_index in range(rows):
        if searched_symbol == matrix[row_index][col_index]:
            position =(row_index, col_index)
            print(position)
            break
    if position:
        break
if not position:
    print(f"{searched_symbol} does not occur in the matrix")

# Decision with functions:--> the fastest

# def create_matrix(row):
#     matrix = [[0] * int(row) for _ in range(int(row))]
#     return matrix
#
#
# def add_values(matrix):
#     for idx in range(len(matrix)):
#         line = [x for x in input()]
#         matrix[idx] = line
#     return matrix
#
#
# def search_symbol(matrix, symbol):
#     for row in matrix:
#         for cell in row:
#             if cell == symbol:
#                 return matrix.index(row), row.index(cell)
#     return f"{symbol} does not occur in the matrix"
#
#
# print(search_symbol(add_values(create_matrix(input())), input()))


# 06. Symbol in Matrix:--> The slowest
# rows = int(input())
# cols = rows
#
# matrix = []
# found_symbol = False
# symbol_position = None
#
# for i in range(rows):
#     line = [x for x in input()] #list(input())
#     matrix.append(line)
#
# symbol = input()
#
# for row in range(rows):
#     for column in range(cols):
#         current_cell = matrix[row][column]
#         if current_cell == symbol:
#             found_symbol = True
#             symbol_position = [row, column]
#         if found_symbol:
#             break
#
# if found_symbol:
#     print(f"({symbol_position[0]}, {symbol_position[1]})")
# else:
#     print(f"{symbol} does not occur in the matrix")
