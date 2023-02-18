from collections import deque

pizzas = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]

counter = 0
while pizzas and employees:
    pizza_nums = pizzas.popleft()
    if pizza_nums <= 0:
        continue
    if pizza_nums> 10:
        continue
    curr_employee = employees.pop()

    if pizza_nums>curr_employee:
        pizza_nums-=curr_employee
        pizzas.appendleft(pizza_nums)
        counter+=curr_employee
        continue
    else:
        counter+=pizza_nums

if not pizzas:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {counter}')
    print(f'Employees: {", ".join([str(x) for x in employees])}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(x) for x in pizzas])}')
