from collections import deque

input_elements = input().split()
numbers = deque()

operations = {
    "+": lambda a,b: a+b,
    "-": lambda a,b: a-b,
    "*": lambda a,b: a*b,
    "/": lambda a,b: a/b,
}


for element in input_elements:
    if element in "+-*/":
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()
            result = operations[element](first, second)
            numbers.appendleft(result)
    else:
        numbers.append(int(element))

print(numbers.popleft())