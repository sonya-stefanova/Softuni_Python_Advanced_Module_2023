num_sequence = [0, 1]


def create_sequence(n):
    global num_sequence
    if n == 0:
        return []
    elif n == 1:
        return [0]

    num_sequence = [0, 1]
    for i in range(2, n):
        num_sequence.append(num_sequence[-1] + num_sequence[-2])
    return num_sequence


def locate(n):
    if n in num_sequence:
        return f"The number -  {n} is at index {num_sequence.index(n)}"
    else:
        return f"The number {n} is not in the sequence"