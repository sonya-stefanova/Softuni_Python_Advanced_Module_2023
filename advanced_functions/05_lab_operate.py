from functools import reduce

dict_of_operations = {
    "+": lambda x, y: x+y,
    "-": lambda x, y: x-y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def operate(operator, *args):
    return reduce(dict_of_operations[operator], args)


# if operator == "+":
#     return reduce(lambda x, y: x+y, args)
# elif operator == "-":
#     return reduce(lambda x, y: x-y, args)
# elif operator == "*":
#     return reduce(lambda x, y: x * y, args)
# elif operator == "/":
#     return reduce(lambda x, y: x / y, args)


print(operate("-", 20, 2, 5))


# Solution3:
from functools import reduce


def operate(operator, *args):
    return reduce(lambda x, y: eval(f'{x} {operator} {y}'), args)


print(operate('+', 2, 2, 6))