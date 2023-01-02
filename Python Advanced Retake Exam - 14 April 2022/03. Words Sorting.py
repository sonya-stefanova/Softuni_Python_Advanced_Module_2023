def words_sorting(*args):
    words_dict = {}

    for word in args:
        if word not in words_dict:
            words_dict[word] = 0
        words_dict[word] +=sum([ord(letter) for letter in word])

    result = ""
    total_sum = sum(words_dict.values())
    if total_sum % 2 !=0:
        for key, value in sorted(words_dict.items(), key=lambda x: (-x[1])):
            result += f"{key} - {value}\n"
    elif total_sum % 2 ==0:
        for key, value in sorted(words_dict.items()):
            result += f"{key} - {value}\n"

    return result




print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))




print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
