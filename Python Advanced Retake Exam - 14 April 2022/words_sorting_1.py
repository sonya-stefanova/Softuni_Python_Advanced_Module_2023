def words_sorting(*args):
    words = {}
    result = []

    for word in args:
        if not word in words:
            words[word] = sum([int(ord(x)) for x in word])

    if not sum(words.values()) % 2 == 0:
        sorted_words = sorted(words.items(), key=lambda kvpt: -kvpt[1])
    else:
        sorted_words = sorted(words.items(), key=lambda kvpt: kvpt[0])

    for el in sorted_words:
        result.append(f"{el[0]} - {el[1]}")
    return "\n".join(result)

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))