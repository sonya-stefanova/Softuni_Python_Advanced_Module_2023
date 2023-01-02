size = int(input())
square_matrix = []

for _ in range(size):
    nums = [int(el) for el in input().split()]
    square_matrix.append(nums)

primary_diagonal_sum = 0
for index in range(size):
    primary_diagonal_sum +=square_matrix[index][index]
print(primary_diagonal_sum)
