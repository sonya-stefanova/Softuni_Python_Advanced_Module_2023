import sys #1Decision =  > Fastest
rows, cols = [int(el) for el in input().split(", ")]

matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]

max_sum = -sys.maxsize
max_sum_list = []

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        flat_sub_matrix = [matrix[row_index][col_index], matrix[row_index][col_index + 1],
                           matrix[row_index+1][col_index], matrix[row_index+1][col_index+1]]

        current_sum = sum(flat_sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_list = flat_sub_matrix.copy()

print(max_sum_list[0], max_sum_list[1])
print(max_sum_list[2], max_sum_list[3])
print(max_sum)


# 07. Square with Maximum Sum:
rows, columns = [int(i) for i in input().split(", ")]
matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]

max_result = -9999999999999999999999999999999999999999
flat_sub_matrix = []

for row in range(rows - 1):
    for column in range(columns - 1):
        top_left = matrix[row][column]
        top_right = matrix[row][column + 1]
        bottom_left = matrix[row + 1][column]
        bottom_right = matrix[row + 1][column + 1]

        result = sum([top_left, top_right, bottom_left, bottom_right])

        if result > max_result:
            max_result = result
            flat_sub_matrix = top_left, top_right, bottom_left, bottom_right

print(flat_sub_matrix[0], flat_sub_matrix[1])
print(flat_sub_matrix[2], flat_sub_matrix[3])
print(max_result)
