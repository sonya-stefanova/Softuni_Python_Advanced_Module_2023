from collections import deque

def gifts_collection(magic_needed, gifts):
    result = magic_needed
    if 100 <= result <= 199:
        gifts['Gemstone'] += 1
    elif 200 <= result <= 299:
        gifts['Porcelain Sculpture'] += 1
    elif 300 <= result <= 399:
        gifts['Gold'] += 1
    elif 400 <= result <= 499:
        gifts['Diamond Jewellery'] += 1
    return gifts

def min_gifts_are_crafted(gifts):
    if gifts['Gemstone'] > 0 and gifts['Porcelain Sculpture'] > 0:
        return True
    elif gifts['Gold'] > 0 and gifts['Diamond Jewellery'] > 0:
        return True
    else:
        return False


materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0}

while True:
    if not materials or not magic_levels:
        break
    current_material = materials.pop()
    current_magic_level = magic_levels.popleft()
    magic_needed = current_material + current_magic_level

    if magic_needed < 100 and magic_needed % 2 == 0:
        magic_needed = current_material * 2 + current_magic_level * 3
        if magic_needed < 100 or magic_needed > 499:
            continue
        else:
            gifts_collection(magic_needed, gifts)

    elif magic_needed < 100 and magic_needed % 2 != 0:
        magic_needed *= 2
        if magic_needed < 100 or magic_needed > 499:
            continue
        else:
            gifts_collection(magic_needed, gifts)
    elif magic_needed > 499:
        magic_needed /= 2
        if magic_needed < 100 or magic_needed > 499:
            continue
        else:
            gifts_collection(magic_needed, gifts)

    else:
        gifts_collection(magic_needed, gifts)

if min_gifts_are_crafted(gifts):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

sorted_gifts = dict(x for x in (sorted(gifts.items(), key=lambda x: x[0])) if x[1] > 0)
for key, value in sorted_gifts.items():
    print(f"{key}: {value}")