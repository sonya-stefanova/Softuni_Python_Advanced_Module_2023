from _collections import deque

seats = input().split(", ")
matched_seats = []
first_seq = deque(int(x) for x in input().split(", ")) #take first
second_seq = deque([int(x) for x in input().split(", ")]) #take last
rotation = 1

while first_seq and second_seq:

    f = first_seq.popleft()
    s = second_seq.pop()

    char= chr(f+s)
    var_1 = f"{f}{char}"
    var_2 = f"{s}{char}"

    if var_1 in seats:
        matched_seats.append(var_1)
        seats.remove(var_1)

    elif var_2 in seats:
        matched_seats.append(var_2)
        seats.remove(var_2)

    else:
        first_seq.append(f)
        second_seq.appendleft(s)


    if len(matched_seats) == 3:
        break

    if rotation == 10:
        break

    rotation+=1

print(f'Seat matches: {", ".join(matched_seats)}')
print(f'Rotations count: {rotation}')

