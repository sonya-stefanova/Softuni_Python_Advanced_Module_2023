n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(' ')])

primary_diagonal = []
secondary_diagonal = []

for idx in range(n):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][n - 1 - idx])

primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)

print(abs(primary_sum - secondary_sum))
