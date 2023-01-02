numbers = input().split()
while numbers:
    last_num = numbers.pop()
    print(last_num, end=" ")
#
# reverse = ""
# while numbers:
#     last_num = numbers.pop()
#     reverse += last_num + " "
# print(reverse)

numbers = [int(x) for x in input().split()]
reversed = []
while numbers:
    reversed.append(numbers.pop())
print(*reversed, sep = " ")
