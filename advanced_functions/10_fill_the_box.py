# def fill_the_box(height, length, width, *args):
#     total_volume = height * length * width
#     left_cubes = 0
#
#     for el in args:
#         if el == 'Finish':
#             break
#
#         if total_volume >= el:
#             total_volume -= el
#         else:
#             el -= total_volume
#             left_cubes += el
#             total_volume = 0
#
#     if total_volume:
#         return f'There is free space in the box. You could put {total_volume} more cubes.'
#     else:
#         return f'No more free space! You have {left_cubes} more cubes.'


def fill_the_box(height, length, width, *args):
    volume = height * length * width

    for num in args:
        if num == "Finish":
            break
        volume -= num

    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {abs(volume)} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
