from collections import deque

def matches(seats, option):
    if option in seats:
        return True

seats = input().split(', ')
first_seq = deque([int(x) for x in input().split(', ')])
second_seq = deque([int(x) for x in input().split(', ')])

seats_matched = []
count_rotations = 0
matches_reached = False
rotations_reached = False

while True:
    count_rotations+=1

    curr_first = first_seq.popleft()
    curr_second = second_seq.pop()
    sum_fs = curr_second+curr_first
    ascii_char = chr(sum_fs)

    first_option = str(curr_first)+ascii_char
    second_option = str(curr_second)+ascii_char

    if matches(seats, first_option):
        seats.remove(first_option)
        seats_matched.append(first_option)
    elif matches(seats, second_option):
        seats.remove(second_option)
        seats_matched.append(second_option)
    else:
        first_seq.append(curr_first)
        second_seq.appendleft(curr_second)


    if len(seats_matched)==3:
        matches_reached = True
        break

    if count_rotations == 10:
        rotations_reached = True
        break

if rotations_reached or matches_reached:
    print(f'Seat matches: {", ".join(seats_matched)}')
    print(f'Rotations count: {count_rotations}')


