# def even_odd(*args):
#     instruction = args[-1]
#     parity = 0 if instruction == 'even' else 1
#
#     result = []
#     for idx in range(len(args) - 1):
#         number = args[idx]
#         if number % 2 == parity:
#             result.append(number)
#
#     return result


def odd_or_even(odd_even: str, *args):

    if odd_even == 'Odd':
        sum_of_num_args = sum([int(x) for x in args if int(x) % 2 != 0])
    elif odd_even == 'Even':
        sum_of_num_args = sum([int(x) for x in args if int(x) % 2 == 0])

    print(sum_of_num_args * len(args))


command = input()
numbers = input().split()
odd_or_even(command, *numbers)