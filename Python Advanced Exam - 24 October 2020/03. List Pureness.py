from collections import deque

def best_list_pureness(numbers_list, rotations):
    numbers_list = deque(numbers_list)
    best_pureness_dict = {}


    for curr_rotation in range(rotations + 1):
        pureness = 0

        for idx, num in enumerate(numbers_list):
            pureness += num * idx

        best_pureness_dict[curr_rotation] = pureness
        numbers_list.rotate(1)

    for rotations, pureness_ in sorted(best_pureness_dict.items(), key=lambda x: -x[1], x[0]):
        return f'Best pureness {pureness_} after {rotations} rotations'

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
