def words_sorting(*args:str):
    words = {}
    for word in args:
        words[word] = sum([ord(letter) for letter in word])

    total_values = sum(words.values())
    if total_values % 2 != 0:
        sorted_dict = sorted(words.items(), key = lambda x: -x[1])
    else:
        sorted_dict = sorted(words.items(), key = lambda x: x[0])

    result = ''
    for k, v in sorted_dict:
        result += f"{k} - {v}\n"
    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
