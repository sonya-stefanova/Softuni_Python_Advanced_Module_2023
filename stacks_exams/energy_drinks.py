from collections import deque

caffeine = deque(int(x) for x in input().split(", ")) #take last caffeine
energy_drinks = deque(int(x) for x in input().split(", ")) #first_energy_dring
stamats_caffeine = 0

MAX_MG = 300

while caffeine and energy_drinks:
    curr_caffeine = caffeine.pop()
    curr_energy_drink = energy_drinks.popleft()

    total = curr_caffeine*curr_energy_drink
    if total+stamats_caffeine<=MAX_MG:
        stamats_caffeine+=total
    else:
        energy_drinks.append(curr_energy_drink)
        deduction = 30
        if stamats_caffeine-deduction>=0:
            stamats_caffeine-=deduction

if energy_drinks:
    print(f'Drinks left: {", ".join([str(d) for d in energy_drinks])}')
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamats_caffeine} mg caffeine.")