from collections import deque

bombs_effects = deque([int(x) for x in input().split(", ")])
bombs_casings = [int(x) for x in input().split(", ")]

bombs_dict = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120
}

crafted_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}
bombs_are_crafted = False

while bombs_effects and bombs_casings:
    bomb_effect = bombs_effects.popleft()
    bomb_casing = bombs_casings.pop()
    total_sum = bomb_effect + bomb_casing

    if total_sum == 40:
        crafted_bombs["Datura Bombs"] += 1
    elif total_sum == 60:
        crafted_bombs["Cherry Bombs"] += 1
    elif total_sum == 120:
        crafted_bombs["Smoke Decoy Bombs"] += 1
    else:
        bomb_casing -= 5
        bombs_effects.appendleft(bomb_effect)
        bombs_casings.append(bomb_casing)

    if crafted_bombs["Datura Bombs"] >= 3 \
            and crafted_bombs["Cherry Bombs"] >= 3 \
            and crafted_bombs["Smoke Decoy Bombs"] >= 3:
        bombs_are_crafted = True
        break

if bombs_are_crafted:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bombs_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bombs_effects])}")
else:
    print("Bomb Effects: empty")
if bombs_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bombs_casings])}")
else:
    print("Bomb Casings: empty")

print(f'Cherry Bombs: {crafted_bombs["Cherry Bombs"]}')
print(f'Datura Bombs: {crafted_bombs["Datura Bombs"]}')
print(f'Smoke Decoy Bombs: {crafted_bombs["Smoke Decoy Bombs"]}')