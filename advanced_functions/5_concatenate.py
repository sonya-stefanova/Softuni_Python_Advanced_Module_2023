def concatenate(*args:str, **kwargs):
    result = ""
    for el in args:
        result +=el
    for key, value in kwargs.items():
        result = result.replace(key, value)
    return result




print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))


# def concatenate(*args, **kwargs):
#     text = ''.join(args)
#
#     for key, value in kwargs.items():
#         text = text.replace(key, value)
#
#     return text