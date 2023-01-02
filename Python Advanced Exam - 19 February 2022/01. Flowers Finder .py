# o e a o e a i
# p r s x r
from collections import deque

vowels = deque(input().split())
consonants = input().split()

dict_of_words={
    "rose": "rose",
    "tulip":"tulip",
    "lotus":"lotus",
    "daffodil":"daffodil"
}

word_found = False
sought_word = ""

while consonants and vowels:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for word in dict_of_words.keys():
        if vowel in dict_of_words[word]:
            dict_of_words[word] = dict_of_words[word].replace(vowel, "")
        if consonant in dict_of_words[word]:
            dict_of_words[word] = dict_of_words[word].replace(consonant, "")

        if dict_of_words[word] == "":
            word_found=True
            sought_word = word
            break

    if word_found:
        break


if word_found:
    print(f"Word found: {sought_word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')