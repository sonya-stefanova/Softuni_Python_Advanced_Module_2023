def get_magic_triangle(n):
    magic_triangle = [[1], [1, 1]]
    for i in range(2, n):
        row = [1]
        for j in range(1, len(magic_triangle[i-1])):
            row.append(magic_triangle[i-1][j-1] + magic_triangle[i-1][j])
        row.append(1)
        magic_triangle.append(row)
    return magic_triangle