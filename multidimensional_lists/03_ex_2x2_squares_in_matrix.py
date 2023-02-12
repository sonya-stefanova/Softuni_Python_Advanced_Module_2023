rows, cols = [int(x) for x in input().split()]

# matrix = []
#
# for _ in range(rows):
#     matrix.append(input().split())
matrix = [input().split() for _ in range(rows)]

matched_squares = 0

#Traversing the : up, down, left, right:
for curr_row in range(rows-1):
    for curr_col in range (cols-1):

        if matrix[curr_row][curr_col] == matrix [curr_row][curr_col+1] == matrix[curr_row +1][curr_col] == matrix[curr_row+1][curr_col+1]:
            matched_squares+=1

print(matched_squares)
