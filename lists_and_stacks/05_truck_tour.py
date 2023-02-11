from collections import deque

petrol_pumps_number = int(input())
pumps = deque()

# Add the petrol detail in the empty queue
for _ in range(petrol_pumps_number):
    pump_data = [int(x) for x in input().split()]
    pumps.append(pump_data)
# Loop through each of the pump details:
for attempt in range(petrol_pumps_number):
    tank = 0
    failed = False
    for fuel, needed_litres in pumps:
        tank += fuel
        if needed_litres > tank:
            failed = True
            break
        else:
            tank -= needed_litres

    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break