first = set([int(x) for x in input().split()])
second = set([int(y) for y in input().split()])
num = int(input())


for _ in range(num):
    command_arguments = input().split()
    command = command_arguments[0]
    set = command_arguments[1]
    if command=="Add":
        if set == "First":
            [first.add(int(x)) for x in command_arguments[2:]]
        else:
            [second.add(int(x)) for x in command_arguments[2:]]
    elif command == "Remove":
        if set == "First":
            first = first.difference([int(x) for x in command_arguments[2:]])
        else:
            second = second.difference([int(x) for x in command_arguments[2:]])
    elif command.startswith("Check"):
        print(first.issubset(second) or second.issubset(first))
print(*sorted(first), sep = ", ")
print(*sorted(second), sep = ", ")
