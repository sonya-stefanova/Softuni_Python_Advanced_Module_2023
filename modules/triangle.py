def print_triangle(num):
    for row_num in range(1, num + 1):
        for curr_num in range(1, row_num + 1):
            print(curr_num, end=' ')
        print()
    for row_num in range(num - 1, 0, -1):
        for curr_num in range(1, row_num + 1):
            print(curr_num, end=' ')
        print()