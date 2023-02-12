import re

SIZE = 6
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(SIZE)]

pattern = r"\d"
curr_row, curr_col = [int(x) for x in re.findall(pattern, input())]
#instead of regex:
# [int(x) for x in input() if x.isdigit()]
directions_mapper = {
    'up': lambda x, y: [x - 1, y],
    'down':lambda x, y: [x + 1, y],
    'left':lambda x, y: [x, y - 1],
    'right': lambda x, y: [x, y + 1]
}

commands = input()
while "Stop" not in commands:
    commands = commands.split(", ")
    if "Create" in commands:
        direction=commands[1]
        value = int(commands[2]) if commands[2].isdigit() else commands[2]
        curr_row, curr_col = directions_mapper[direction](curr_row, curr_col)
        if matrix[curr_row][curr_col] == ".":
            matrix[curr_row][curr_col] = value
    elif 'Update' in commands:
        direction=commands[1]
        value = int(commands[2]) if commands[2].isdigit() else commands[2]
        curr_row, curr_col = directions_mapper[direction](curr_row, curr_col)
        if matrix[curr_row][curr_col] != ".":
            matrix[curr_row][curr_col] = value
    elif 'Delete' in commands:
        direction = commands[1]
        curr_row, curr_col = directions_mapper[direction](curr_row, curr_col)
        if matrix[curr_row][curr_col] != ".":
            matrix[curr_row][curr_col] = "."
    elif 'Read' in commands:
        direction = commands[1]
        curr_row, curr_col = directions_mapper[direction](curr_row, curr_col)
        if matrix[curr_row][curr_col] != ".":
            print(matrix[curr_row][curr_col])

    commands = input()

[print(*row, sep = " ") for row in matrix]