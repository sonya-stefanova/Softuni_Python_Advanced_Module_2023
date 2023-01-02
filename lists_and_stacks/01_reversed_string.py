# initial_string = input()
#
# stack = []
#
# for i in range(len(initial_string)):
#     each_letter = initial_string[i]
#     stack.append(each_letter)
#
# reversed_string = ""
#
# while stack:
#     reversed_string+=stack.pop()
#
# print(reversed_string)

initial_string = input()

stack = []

for each_letter in initial_string:
    stack.append(each_letter)

reversed_string = ""

while stack:
    last_letter = stack[-1]
    reversed_string+=last_letter
    stack.pop()

print(reversed_string)


# Solution without stack
# input_line = input()
#
# reversed_string = "".join(list(reversed(input_line)))
#
# print(reversed_string)