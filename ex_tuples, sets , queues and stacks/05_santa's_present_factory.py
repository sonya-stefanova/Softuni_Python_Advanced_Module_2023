from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])

crafting_table = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted_toys = {}

while materials and magic_values:
    current_material = materials.pop()
    current_magic_level = magic_values.popleft()

    if current_material == 0 and current_magic_level == 0:
        continue

    if current_material == 0:
        magic_values.appendleft(current_magic_level)
        continue

    if current_magic_level == 0:
        materials.append(current_material)
        continue

    result = current_material * current_magic_level
    if result in crafting_table:
        toy_name = crafting_table[result]
        if toy_name not in crafted_toys:
            crafted_toys[toy_name]= 0
        crafted_toys[toy_name] = 1
        continue

    if result < 0:
        materials.append(current_material + current_magic_level)
    else:
        materials.append(current_material + 15)

if 'Doll' in crafted_toys and 'Wooden train' in crafted_toys or 'Teddy bear' in crafted_toys and 'Bicycle' in crafted_toys:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")

if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

for present, count in sorted(crafted_toys.items()):
    print(f'{present}: {count}')