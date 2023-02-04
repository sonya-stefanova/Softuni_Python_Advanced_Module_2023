from collections import deque


def best_list_pureness(*test):
    list_of_nums = test[0]
    list_of_nums = deque([int(x) for x in list_of_nums])

    number = int(test[1])
    dict = {}
    for current_rotation in range(number+1):

        new_list = []
        total = 0
        best_rotation = 0
        best_pureness = 0

        for idx, value in enumerate(list_of_nums):
            new_list.append(idx * value)
            total = sum(new_list)
        if best_pureness <= total:
            best_pureness = total
            best_rotation = current_rotation
        dict[current_rotation] = best_pureness

        list_of_nums.rotate(1)

    for k,v in dict.items():
        max_value = max(dict.values())
        max_key = max(dict, key = dict.get)
        return f'Best pureness {max_value} after {max_key} rotations'


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
