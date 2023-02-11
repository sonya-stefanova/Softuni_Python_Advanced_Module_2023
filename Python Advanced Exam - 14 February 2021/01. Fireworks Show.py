
from collections import deque

firework_effects = deque([int(x) for x in input().split(', ')])
explosive_power = [int(x) for x in input().split(', ')]

is_done = False

fireworks = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}

while True:

    if fireworks['Palm Fireworks'] >= 3 and fireworks['Willow Fireworks'] >= 3 \
            and fireworks['Crossette Fireworks'] >= 3:
        is_done = True
        break
    if not firework_effects or not explosive_power:
        break
    current_effect = firework_effects.popleft()
    if current_effect <= 0:
        continue

    current_power = explosive_power.pop()
    if current_power <= 0:
        firework_effects.appendleft(current_effect)
        continue

    mix = current_effect + current_power

    if mix % 3 == 0 and mix % 5 != 0:
        fireworks['Palm Fireworks'] += 1
    elif mix % 5 == 0 and mix % 3 != 0:
        fireworks['Willow Fireworks'] += 1
    elif mix % 3 == 0 and mix % 5 == 0:
        fireworks['Crossette Fireworks'] += 1
    else:
        current_effect -= 1
        firework_effects.append(current_effect)
        explosive_power.append(current_power)

if is_done:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")
for key, value in fireworks.items():
    print(f"{key}: {value}")