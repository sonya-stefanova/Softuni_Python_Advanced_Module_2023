size = int(input())
racing_number = input()
matrix = []

for _ in range(size):
    matrix.append(input().split())

curr_row, curr_col = 0, 0
total_km = 0
direction = input()

while direction:

    if direction == 'End':
        print(f'Racing car {racing_number} DNF.')
        break

    if direction == 'up':
        curr_row -= 1
    elif direction == 'down':
        curr_row += 1
    elif direction == 'left':
        curr_col -= 1
    elif direction == 'right':
        curr_col += 1


    if matrix[curr_row][curr_col] == '.':
        total_km += 10

    elif matrix[curr_row][curr_col] == 'T':
        matrix[curr_row][curr_col] = '.'
        for r in range(size):
            for c in range(size):
                if matrix[r][c] == 'T':
                    matrix[r][c] = '.'
                    curr_row, curr_col = r, c
        total_km += 30

    elif matrix[curr_row][curr_col] == 'F':
        total_km += 10
        print(f'Racing car {racing_number} finished the stage!')
        break
    direction = input()

matrix[curr_row][curr_col] = 'C'

print(f'Distance covered {total_km} km.')

for row in matrix:
    print(*row, sep = "")