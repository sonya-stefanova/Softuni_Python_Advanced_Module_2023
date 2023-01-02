stack = []
operation_count = int(input())

for _ in range(operation_count):
    query_parts = [int(x) for x in input().split()]
    command = query_parts[0]
    if command == 1:
        number = query_parts[1]
        stack.append(number)
    elif command ==2 and stack:
        stack.pop()
    elif command ==3 and stack:
        print(max(stack))
    elif command == 4 and stack:
        print(min(stack))
# reversed_stack = stack[::-1]
reversed_stack = []
while stack:
    reversed_stack.append(str(stack.pop()))

print(", ".join(reversed_stack))



# stack = []
# n = int(input())
# for _ in range(n):
#     command = input().split()
#     if "1" in command:
#         stack.append(int(command[1]))
#     elif "2" in command and stack:
#         stack.pop()
#     elif "3" in command and stack:
#         print(max(stack))
#     elif "4" in command and stack:
#         print(min(stack))
# reversed = []
# while stack:
#     reversed.append(stack.pop())
# print(*reversed, sep = " ")