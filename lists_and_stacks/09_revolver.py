from collections import deque

price_per_bullet = int(input())
initial_gun_barrel = int(input())
available_bullets = [int(x) for x in input().split()]
locks_for_shooting = deque([int(x) for x in input().split()])
intelligence_value = int(input())

shot_bullets = 0
gun_barrel_counter = initial_gun_barrel

while True:
    if not available_bullets or not locks_for_shooting:
        break

    shot_bullet = available_bullets.pop()

    if gun_barrel_counter > 0:
        if shot_bullet <= locks_for_shooting[0]:
            print('Bang!')
            locks_for_shooting.popleft()
        else:
            print('Ping!')
        gun_barrel_counter -= 1
        shot_bullets += 1

    if gun_barrel_counter == 0 and available_bullets:
        print('Reloading!')
        gun_barrel_counter = initial_gun_barrel

if locks_for_shooting:
    print(f"Couldn't get through. Locks left: {len(locks_for_shooting)}")
else:
    money = intelligence_value - (price_per_bullet * shot_bullets)
    print(f"{len(available_bullets)} bullets left. Earned ${money}")