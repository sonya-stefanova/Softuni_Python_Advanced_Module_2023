from collections import deque

food_quantity = int(input())

orders = deque([int(x) for x in input().split()])
biggest_order = max(orders)

not_enough_food = False
while orders:
    current_order = orders[0]
    if current_order>food_quantity:
        not_enough_food = True
        break
    food_quantity-=current_order
    orders.popleft()

orders = [str(x) for x in orders]
print(biggest_order)

if orders:
    print(f"Orders left: {' '.join(orders)}")
else:
    print("Orders complete.")

