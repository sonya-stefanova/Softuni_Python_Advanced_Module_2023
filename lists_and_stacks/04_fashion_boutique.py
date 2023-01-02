clothes = [int(x) for x in input().split()]
max_capacity = int(input())

rack_counter = 1
current_capacity = max_capacity

while clothes:
    current_piece = clothes[-1]

    if current_piece <= current_capacity:
        clothes.pop()
        current_capacity -= current_piece
    else:
        rack_counter += 1
        current_capacity = max_capacity

print(rack_counter)