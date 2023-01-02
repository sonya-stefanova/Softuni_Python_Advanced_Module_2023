from calcs_2 import calc

first_num, operator, second_num = [float(x) if x.isdigit() else x for x in input().split()]

print(calc(first_num, operator, second_num))