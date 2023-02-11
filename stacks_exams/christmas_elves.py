from collections import deque

elfs_energy = deque([int(x) for x in input().split()])
materials_in_box = [int(x) for x in input().split()]

toys = 0
used_energy = 0
days = 0

while elfs_energy and materials_in_box:

    if elfs_energy[0] < 5:
        elfs_energy.popleft()
        continue

    if not elfs_energy:
        break

    current_elf_energy = elfs_energy.popleft()
    current_box = materials_in_box.pop()

    days += 1

    toys_to_be_created = 1
    energy_consumption = current_box
    cookie = 1

    if days % 3 == 0:
        toys_to_be_created = 2
        energy_consumption *= 2

    if days % 5 == 0:
        toys_to_be_created = 0
        cookie = 0

    if energy_consumption <= current_elf_energy:
        toys += toys_to_be_created
        used_energy += energy_consumption
        elfs_energy.append(current_elf_energy - energy_consumption + cookie)
    else:
        materials_in_box.append(current_box)
        elfs_energy.append(current_elf_energy * 2)


print(f"Toys: {toys}")
print(f"Energy: {used_energy}")
if elfs_energy:
    print(f"Elves left: {', '.join([str(x) for x in elfs_energy])}")
if materials_in_box:
    print(f"Boxes left: {', '.join([str(x) for x in materials_in_box])}")
