from collections import deque


def under_100(magic_needed, material, magic):
    parity = True if magic_needed % 2 == 0 else False
    if parity:
        material *= 2
        magic *= 3
    else:
        material *= 2
        magic *= 2
    magic_needed = material + magic
    if magic_needed>=100:
        return gift_making(magic_needed)
    return

def over_499(magic_needed, material, magic):
    material /=2
    magic /=2
    magic_needed = material+magic
    if magic_needed<=499:
        return gift_making(magic_needed)
    return

def gift_making(magic_needed):
    if magic_needed < 100:
        under_100(current_magic, current_material, current_magic)
    elif 100 <= magic_needed <= 199:
        gifts["Gemstone"]+=1
    elif magic_needed <= 299:
        gifts["Porcelain Sculpture"]+=1
    elif magic_needed <= 399:
        gifts["Gold"]+=1
    elif magic_needed <= 499:
        gifts["Diamond Jewellery"]+=1
    elif magic_needed>500:
        over_499(magic_needed, current_magic, current_material)
    return gifts


materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])
gifts_crafting_finished = False

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture":0,
    "Gold": 0,
    "Diamond Jewellery":0
}

while True:
    if not materials or not magic:
        break
    current_material = materials.pop()
    current_magic = magic.popleft()

    magic_needed = current_magic + current_material
    gift_making(magic_needed)
    if (gifts["Gemstone"] and gifts["Porcelain Sculpture"])>=1 or (gifts["Gold"] and gifts["Diamond Jewellery"])>=1:
        gifts_crafting_finished = True

if gifts_crafting_finished:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials])}')
if magic:
    print(f'Magic left: {", ".join([str(x) for x in magic])}')

result = ""
for gift, counter in sorted(gifts.items()):
    if counter>0:
        result += f"{gift}: {counter}\n"
print(result)

