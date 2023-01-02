numbers = [int(x) for x in input().split()]

positives = [x for x in numbers if x>0]
negatives = [x for x in numbers if x<0]

print(sum(negatives))
print(sum(positives))

if sum(positives)>sum([abs(x) for x in negatives]):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")


# def diff_nums(*args) -> None:
#     sum_positive = sum([int(x) for x in args if int(x) > 0])
#     sum_negative = sum([int(x) for x in args if int(x) < 0])
#     print(sum_negative)
#     print(sum_positive)
#     if abs(sum_negative) > abs(sum_positive):
#         print('The negatives are stronger than the positives')
#     if abs(sum_negative) < abs(sum_positive):
#         print('The positives are stronger than the negatives')
#
#
# input_line = input().split()
# diff_nums(*input_line)
