from collections import deque

elves_energy = deque([int(i) for i in input().split()])
boxes_of_materials = [int(i) for i in input().split()]
used_energy = 0
toys = 0
time = 0

while elves_energy and boxes_of_materials:

    while elves_energy and elves_energy[0] < 5:
        elves_energy.popleft()

    if not elves_energy:
        break

    current_energy = elves_energy.popleft()
    current_box = boxes_of_materials.pop()
    time += 1

    toys_created_count = 1
    needed_energy = current_box
    energy_factory = 1

    if time % 3 == 0:
       toys_created_count = 2
       needed_energy *= 2

    if time % 5 == 0:
        toys_created_count = 0
        energy_factory = 0

    if needed_energy <= current_energy:
        toys += toys_created_count
        used_energy += needed_energy
        elves_energy.append(current_energy - needed_energy + energy_factory)
    else:
        boxes_of_materials.append(current_box)
        elves_energy.append(current_energy * 2)


print(f"Toys: {toys}")
print(f"Energy: {used_energy}")

if elves_energy:
    result = ", ".join(map(str, elves_energy))
    print(f"Elves left: {result}")
else:
    result = ", ".join(map(str, boxes_of_materials))
    print(f"Boxes left: {result}")