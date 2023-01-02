from collections import deque

green_light = int(input())
window = int(input())

cars_on_queue = deque()
cars_counter = 0
there_is_a_crash = False

command = input()

while command != "END":
    if command == "green":
        if cars_on_queue:
            current = cars_on_queue.popleft()
            seconds_left = green_light - len(current)
            while seconds_left > 0:
                cars_counter += 1
                if cars_on_queue:
                    current = cars_on_queue.popleft()
                    seconds_left -= len(current)
                else:
                    break
            if seconds_left == 0:
                cars_counter += 1
            if window >= abs(seconds_left):
                if seconds_left < 0:
                    cars_counter += 1
            else:
                idx = window + seconds_left
                print("A crash happened!")
                print(f"{current} was hit at {current[idx]}.")
                there_is_a_crash = True
                break
    else:
        cars_on_queue.append(command)
    command = input()

if not there_is_a_crash:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")
