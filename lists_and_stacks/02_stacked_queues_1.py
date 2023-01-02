query_count = int(input())

stack_of_numbers = []

for _ in range(0, query_count):

    command = input().split()

    if command[0] == '1':
        stack_of_numbers.append(int(command[1]))
    elif command[0] == '2':
        if stack_of_numbers:
            stack_of_numbers.pop()
    elif command[0] == '3':
        if stack_of_numbers:
            print(max(stack_of_numbers))
    elif command[0] == '4':
        if stack_of_numbers:
            print(min(stack_of_numbers))

stack_of_numbers = list(map(str, stack_of_numbers))
print(', '.join(stack_of_numbers[::-1]))