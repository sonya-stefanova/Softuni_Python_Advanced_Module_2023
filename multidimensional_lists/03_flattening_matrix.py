rows = int(input())
matrix = []

for _ in range(rows):
    nums = [int(x) for x in input().split(', ')]
    matrix.extend(nums)
print(matrix)


# rows = int(input())
# matrix = []
#
# for row in range(rows):
#     line = [int(i) for i in input().split(", ")]
#     matrix.append(line)
#
# flattened_matrix = []
# for collection in matrix:
#     for num in collection:
#         flattened_matrix.append(num)
#
# print(flattened_matrix)