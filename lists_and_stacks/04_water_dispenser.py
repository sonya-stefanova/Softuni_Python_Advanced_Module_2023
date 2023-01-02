from collections import deque

water_quantity = int(input())
queue = deque()
command = input()
while command != "Start":
    people = command
    queue.append(people)
    command = input()

action = input()
while action != "End":
    instruction = action.split(" ")

    if "refill" in action:
        litres_needed = int(instruction[1])
        water_quantity+=litres_needed
    else:
        current_person = queue.popleft()
        litres_needed = int(instruction[0])

        if litres_needed <= water_quantity:
            print(f'{current_person} got water')
            water_quantity -= litres_needed
        else:
            print(f'{current_person} must wait')

    action = input()
print(f'{water_quantity} liters left')

