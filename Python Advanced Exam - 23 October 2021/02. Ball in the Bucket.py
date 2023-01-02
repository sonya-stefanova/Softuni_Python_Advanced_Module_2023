def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size

size = 6
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for x in range(size)]
total = 0
throws = 3

for _ in range(throws):
    row, col = [int(x) for x in input() if x.isdigit()]

    if is_valid(row, col, size) and matrix[row][col] == 'B':
        matrix[row][col] = 0
        for r in range(size):
            total += matrix[r][col]

if total < 100:
    print(f"Sorry! You need {100 - total} points more to win a prize.")
else:
    if total <= 199:
        prize = 'Football'
    elif total <= 299:
        prize = 'Teddy Bear'
    elif total >= 300:
        prize = 'Lego Construction Set'
    print(f"Good job! You scored {total} points, and you've won {prize}.")