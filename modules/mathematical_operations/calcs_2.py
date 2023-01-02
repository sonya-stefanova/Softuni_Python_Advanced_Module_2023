def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def pow(a, b):
    return a ** b


operations_mapper = {
    "+": lambda a,b: a+b,
    "-": lambda a,b: a-b,
    "*": lambda a,b: a*b,
    "/": lambda a,b: a/b,
    "^": lambda a,b: a^b
}

def calc(first_num, sign, second_num):
    return f"{operations_mapper[sign](first_num, second_num):.2f}"