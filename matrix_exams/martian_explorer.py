SIZE = 6
directions_mapper = {
    'up': lambda x, y: [x - 1, y],
    'down':lambda x, y: [x + 1, y],
    'left':lambda x, y: [x, y - 1],
    'right': lambda x, y: [x, y + 1]
}
reposition_mapper = {
    'up': lambda x, y: [SIZE - 1, y],
    'down':lambda x, y: [0, y],
    'left':lambda x, y: [x, SIZE - 1],
    'right': lambda x, y: [x, 0]
}
deposits_count = {
    "W": 0,
    "M": 0,
    "C":0
}

matrix = [input().split() for _ in range(SIZE)]
martian_row, martian_col = 0, 0

directions = input().split(", ")

for row in range(len(matrix)):
    if "E" in matrix[row]:
        martian_row, martian_col = [row, matrix[row].index("E")]


for direction in directions:
    martian_row, martian_col = directions_mapper[direction](martian_row, martian_col)
    if not (0 <= martian_row < SIZE and 0 <= martian_col < SIZE):
        martian_row, martian_col = reposition_mapper[direction](martian_row, martian_col)

    if matrix[martian_row][martian_col]=="-":
        pass
    elif matrix[martian_row][martian_col] == "W":
        print(f"Water deposit found at ({martian_row}, {martian_col})")
        deposits_count["W"]+=1
        continue
    elif matrix[martian_row][martian_col]=="C":
        print(f"Concrete deposit found at ({martian_row}, {martian_col})")
        deposits_count["C"]+=1
        continue
    elif matrix[martian_row][martian_col]=="M":
        print(f"Metal deposit found at ({martian_row}, {martian_col})")
        deposits_count["M"]+=1
        continue
    elif matrix[martian_row][martian_col]=="R":
        print(f"Rover got broken at ({martian_row}, {martian_col})")
        break

if deposits_count["W"]>=1 and deposits_count["M"]>=1 and deposits_count["C"]>=1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")


