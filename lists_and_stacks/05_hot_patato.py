stack = []
n = int(input())
for _ in range(n):
    command = input().split(" ")
    num_command = command[0]
    if command == "1":
        number = int(command[1])
        stack.append(number)
    elif command == "2" and stack:
        stack.pop()
    elif command == "3" and stack:
        print(max(stack))
    elif command == "4" and stack:
        print(min(stack))

stack.reverse()
print(stack)