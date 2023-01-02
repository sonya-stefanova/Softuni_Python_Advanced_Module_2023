from collections import deque

bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()] #stack
operators = deque(input().split())

honey_made = 0

honey_making_operations_legend = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

while bees and nectars:
    current_bee = bees.popleft()
    current_nectar = nectars.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
        continue

    if current_nectar == 0:
        continue

    operator = operators.popleft()
    honey_made += abs(honey_making_operations_legend[operator](current_bee, current_nectar))

print(f'Total honey made: {honey_made}')

if bees:
    print(f'Bees left: {", ".join([str(x) for x in bees])}')

if nectars:
    print(f'Nectars left: {", ".join([str(x) for x in nectars])}')