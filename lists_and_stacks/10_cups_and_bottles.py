# 4 2 10 5 - filling from the first cup

# 3 15 15 11 6 bottles = You must start picking from the last received bottle
from collections import deque

from collections import deque


cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted_water = 0

while cups and bottles:
    cup = cups.popleft()
    while cup > 0:
        bottle = bottles.pop()
        cup -= bottle
    else:
        wasted_water += abs(cup)

else:
    if cups:
        print(f"Cups:", ' '.join([str(x) for x in cups]))
    else:
        print(f"Bottles:", ' '.join([str(x) for x in bottles]))

    print(f"Wasted litters of water: {wasted_water}")