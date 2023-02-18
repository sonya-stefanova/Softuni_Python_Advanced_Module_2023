from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

created_healing_items = {}


while textiles and medicaments:

    curr_textile = textiles.popleft()
    curr_medicament = medicaments.pop()

    total = curr_textile + curr_medicament

    if total == 30:
        if "Patch" not in created_healing_items:
            created_healing_items["Patch"] = 0
        created_healing_items["Patch"] += 1

    elif total==40:
        if "Bandage" not in created_healing_items:
            created_healing_items["Bandage"] = 0
        created_healing_items["Bandage"] += 1

    elif total == 100:
        if "MedKit" not in created_healing_items:
            created_healing_items["MedKit"] = 0
        created_healing_items["MedKit"] += 1

    elif total>100:
        if "MedKit" not in created_healing_items:
            created_healing_items["MedKit"] = 0
        created_healing_items["MedKit"] += 1
        difference_resources = abs(total-100)
        medicaments[-1]+=difference_resources

    else:
        curr_medicament+=10
        medicaments.append(curr_medicament)
        continue

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

if len(created_healing_items)>0:
    for item_name, amount_created in sorted(created_healing_items.items(), key = lambda x: (-x[1], x[0])):
        print(f"{item_name} - {amount_created}")

if medicaments:
    meds = []
    while medicaments:
        meds.append(medicaments.pop())
    print(f'Medicaments left: {", ".join([str(x) for x in meds])}')
if textiles:
    print(f'Textiles left: {", ".join([str(x) for x in textiles])}')
