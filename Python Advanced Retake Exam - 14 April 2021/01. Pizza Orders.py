from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')])
employees_capacity = deque([int(x) for x in input().split(', ')])
total_pizzas = 0

while employees_capacity and pizza_orders:

    current_order = pizza_orders.popleft()

    if current_order > 10 or current_order <= 0:
        continue

    current_capacity = employees_capacity.pop()

    if current_capacity >= current_order:
        total_pizzas += current_order

    elif current_capacity < current_order:
        current_order -= current_capacity
        pizza_orders.appendleft(current_order)
        total_pizzas += current_capacity

if employees_capacity:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(str(x) for x in employees_capacity)}")
else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")

