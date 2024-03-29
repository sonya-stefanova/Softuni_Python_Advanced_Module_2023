from collections import deque

order = deque(map(int, input().split(', ')))
employee = [int(el) for el in input().split(', ')]

total_pizza = 0
while order and employee:
    pizza = order.popleft()
    if pizza>10 or pizza<=0:
        continue
    em = employee.pop()
    if pizza <= em:
        total_pizza += pizza
    else:
        order.insert(0, pizza-em)
        total_pizza += em

if not order:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizza}')
    print(f'Employees:', ', '.join(str(el) for el in employee))
else:
    print('Not all orders are completed.')
    print(f'Orders left:', ', '.join(str(el) for el in order))