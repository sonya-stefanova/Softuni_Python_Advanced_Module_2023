def naughty_or_nice_list(children: list, *args, **kwargs):
    final_dict = {"Nice": [], "Naughty": [], "Not found": []}


    for command in args:
        num, behaviour = command.split('-')

        for tuple_ in children:
            if [str(x[0]) for x in children].count(num) == 1 and tuple_[0] == int(num):
                final_dict[behaviour].append(tuple_[1])
                children.remove(tuple_)

    for key, val in kwargs.items():
        for tuple_ in children:
            if [str(x[1]) for x in children].count(key) == 1 and tuple_[1] == key:
                final_dict[val].append(key)
                children.remove(tuple_)

    if children:
        for num, name in children:
            final_dict['Not found'].append(name)

    result = []
    for k, v in final_dict.items():
        if v:
            result.append(f"{k}: {', '.join(v)}")

    return "\n".join(result)

print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))