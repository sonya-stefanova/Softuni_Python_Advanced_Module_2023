n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])

primary_diagonal = []
secondary_diagonal = []

for idx in range(n):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][n - 1 - idx])

print(f'Primary diagonal: {", ".join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')
