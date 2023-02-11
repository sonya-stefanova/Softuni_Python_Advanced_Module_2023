sentence = input()

dict_of_symbols = {}

for symbol in sentence:
    if symbol not in dict_of_symbols:
        dict_of_symbols[symbol] = 0
    dict_of_symbols[symbol] += 1


for kvp in sorted(dict_of_symbols.items()):
    print(f'{kvp[0]}: {kvp[1]} time/s')