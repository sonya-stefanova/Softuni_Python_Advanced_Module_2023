from collections import deque
#NOT SOLVED IN THIS VARIANT YET

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

gifts_collection = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0}

are_crafted= False

gifts = {
    "Gemstone": range(100, 200),
    "Porcelain Sculpture": range(200, 300),
    "Gold": range(300, 400),
    "Diamond Jewellery": range(400, 500)

}
while True:
    if not materials or not magic_levels:
        break

    curr_material = materials.pop()
    curr_magic = magic_levels.popleft()

    needed_magic = curr_magic+curr_material

    def complete_dict(needed_magic, gift_result):
        gifts_collection[k] +=1
        return gifts_collection

    for k, v in gifts.items():
        if needed_magic>=100 and needed_magic<=499:
            complete_dict(needed_magic, gifts_collection)
            break

        elif needed_magic < 100:
            if needed_magic % 2 == 0:
                curr_magic*=3
                curr_material*=2
                needed_magic = curr_magic+curr_material
                complete_dict(needed_magic, gifts_collection)

            else:
                complete_dict(needed_magic*2, gifts_collection)


        else:
            complete_dict(needed_magic/2, gifts_collection)

if ('Gemstone' in gifts_collection.keys() and 'Porcelain Sculpture' in gifts_collection.keys()) \
        or ('Gold' in gifts_collection.keys() and 'Diamond Jewellery' in gifts_collection.keys()):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for k, v in sorted(filter(lambda x: x[1]>0, gifts_collection.items())):
    print(f"{k}: {v}")