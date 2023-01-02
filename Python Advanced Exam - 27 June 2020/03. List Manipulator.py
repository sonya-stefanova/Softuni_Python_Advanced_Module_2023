def list_manipulator(list_of_numbers, first_command, second_command, *args):
    if first_command == 'add' and second_command == 'beginning':
        args = list(args)
        args.extend(list_of_numbers)
        return args
    elif first_command == 'add' and second_command == 'end':
        list_of_numbers.extend(args)
        return list_of_numbers
    elif first_command == 'remove' and second_command == 'beginning':
        if args:
            num = args[0]
            for i in range(num):
                list_of_numbers.pop(0)
        else:
            list_of_numbers.pop(0)
        return list_of_numbers
    elif first_command == 'remove' and second_command == 'end':
        if args:
            num = args[0]
            for i in range(num):
                list_of_numbers.pop()
        else:
            list_of_numbers.pop()
        return list_of_numbers

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

#
# def list_manipulator(list_elements, *args):
#     result = []
#     command = args[0]
#     command_arg = args[1]
#     new_elements = []
#     if len(args) > 2:
#         new_elements = list(args[2:])
#     if command == 'remove' and command_arg == 'beginning' and new_elements:
#         index = new_elements[0]
#         return list_elements[index:]
#     if command == 'remove' and command_arg == 'end' and new_elements:
#         index = new_elements[0]
#         return list_elements[:-index]
#     if command == 'remove' and command_arg == 'end':
#         size = len(list_elements)
#         return list_elements[:size - 1]
#     if command == 'remove' and command_arg == 'beginning':
#         return list_elements[1:]
#     if command == 'add' and command_arg == 'beginning':
#         return new_elements + list_elements
#     if command == 'add' and command_arg == 'end':
#         return list_elements + new_elements
#
#
# print(list_manipulator([1, 2, 3], "remove", "end"))
# print(list_manipulator([1, 2, 3], "remove", "beginning"))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20))
# print(list_manipulator([1, 2, 3], "add", "end", 30))
# print(list_manipulator([1, 2, 3], "remove", "end", 2))
# print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))