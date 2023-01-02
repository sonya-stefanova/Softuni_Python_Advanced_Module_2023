from collections import deque


customers = deque([int(x) for x in input().split(", ")])
taxies = [int(x) for x in input().split(", ")]
total_time = 0
while True:
    if not customers or not taxies:
        break
    current_customer_time = customers.popleft()
    current_taxi_time = taxies.pop()

    if current_customer_time<=current_taxi_time:
        total_time+=current_customer_time
    else:
        customers.appendleft(current_customer_time)

if not customers:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
elif customers and not taxies:
    print(f'Not all customers were driven to their destinations\nCustomers left: {", ".join([str(x) for x in customers])}')



