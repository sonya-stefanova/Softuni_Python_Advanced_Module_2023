PUSH = "1"
DELETE = "2"
MAX = "3"
MIN = "4"


def push(n, stack):
    stack.append(n)
    return stack


def delete(stack):
    stack.pop()
    return stack


def calc_max(stack):
    max_n = max([int(el) for el in stack])
    return max_n


def calc_min(stack):
    min_n = min([int(el) for el in stack])
    return min_n


def stacked_queues(num_commands):
    stack = []
    result = []

    for _ in range(num_commands):
        command = input()
        if command.startswith(PUSH):
            query = command.split(" ")
            num = push(query[1], stack)
        elif command == DELETE and stack:
            num = delete(stack)
        elif command == MAX and stack:
            print(calc_max(stack))
        elif command == MIN and stack:
            print(calc_min(stack))

    while stack:
        result.append(stack.pop())

    print(f"{', '.join(result)}")

commands = int(input())
stacked_queues(commands)