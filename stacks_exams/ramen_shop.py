from _collections import deque

bowls_of_ramen = [int(x) for x in input().split(", ")] #take last
customers = deque([int(x) for x in input().split(", ")]) #take first

while bowls_of_ramen and customers:
    bowl = bowls_of_ramen.pop()
    customer = customers.popleft()

    if bowl > customer:
        bowl-=customer
        bowls_of_ramen.append(bowl)
        continue

    elif bowl < customer:
        customer-=bowl
        customers.appendleft(customer)
        continue

if len(customers) == 0:
    print(f"Great job! You served all the customers.")
else:
    print("Out of ramen! You didn't manage to serve all customers.")

if bowls_of_ramen:
    print(f"Bowls of ramen left: {', '.join([str(b) for b in bowls_of_ramen])}")
if customers:
    print(f"Customers left: {', '.join([str(c) for c in customers])}")


