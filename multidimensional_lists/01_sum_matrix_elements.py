rows, cols = [int(x) for x in input().split(', ')]
matrix = []
output = 0

for _ in range(rows):
    nums = [int(x) for x in input().split(', ')]
    output += sum(nums)
    matrix.append(nums)

print(output)
print(matrix)
