from collections import deque

input_elements = input().split()
numbers = deque()

for element in input_elements:
    if element in "+-*/":
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()

            if element == '+':
                result = first + second
            elif element == '-':
                result = first - second
            elif element == '*':
                result = first * second
            elif element == '/':
                result = first // second

            numbers.appendleft(result)
    else:
        numbers.append(int(element))

print(numbers.popleft())


