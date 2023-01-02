from collections import deque

chocolates = [int(x) for x in input().split(', ') if int(x)>0] #this is a stack because we only operate with the last chockolate
milk_cups = deque([int(x) for x in input().split(', ') if int(x)>0])
max_milkshakes = 5

done_milkshakes_counter = 0

while chocolates and milk_cups and done_milkshakes_counter < max_milkshakes:
    last_chocolate = chocolates.pop()
    last_milk_cup = milk_cups.popleft()

    if last_chocolate <= 0 and last_milk_cup <= 0:
        continue

    if last_chocolate <= 0:
        milk_cups.appendleft(last_milk_cup)
        continue

    if last_milk_cup <= 0:
        chocolates.append(last_chocolate)
        continue

    if last_chocolate == last_milk_cup:
        done_milkshakes_counter += 1
    else:
        chocolates.append(last_chocolate - 5)
        milk_cups.append(last_milk_cup)

if done_milkshakes_counter == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolates:
    print(f'Chocolate: {", ".join([str(x) for x in chocolates])}')
else:
    print(f'Chocolate: empty')

if milk_cups:
    print(f'Milk: {", ".join([str(x) for x in milk_cups])}')
else:
    print(f'Milk: empty')