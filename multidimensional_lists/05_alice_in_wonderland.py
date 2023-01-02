def next_position_calc(row, col, command):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1


def is_outside(row, col, size):
    return row < 0 or row >= size or col < 0 or col >= size or matrix[alice_row][alice_col]=="R"


size = int(input())
matrix = []
alice_row, alice_col = 0, 0
total_bags = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == 'A':
            alice_row = row
            alice_col = col

command = input()
out_of_territory = False

while command:
    matrix[alice_row][alice_col] = "*"
    alice_row, alice_col = next_position_calc(alice_row, alice_col, command)

    if is_outside(row, col, size):
        out_of_territory = True
        matrix[alice_row][alice_col] = "*"
        break

    if matrix[alice_row][alice_col].isdigit():
        total_bags+=int(matrix[alice_row][alice_col])
        matrix[alice_row][alice_col] = "*"

        if total_bags>=10:
            break

    command = input()


if out_of_territory:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for row in matrix:
    print(*row, sep= " ")