from collections import deque

coffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque([int(x) for x in input().split(', ')])

total_coffeine = 0
max_caffein = 300

while coffeine and energy_drinks:
    current_coffeine = coffeine.pop()
    current_energy_drink = energy_drinks.popleft()

    current_doze = current_coffeine * current_energy_drink

    if current_doze + total_coffeine <= max_caffein:
        total_coffeine += current_doze
    else:
        energy_drinks.append(current_energy_drink)
        if total_coffeine<30:
            total_coffeine = 0
        total_coffeine -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

if total_coffeine >= 0:
    print(f"Stamat is going to sleep with {total_coffeine} mg caffeine.")
else:
    print(f"Stamat is going to sleep with 0 mg caffeine.")