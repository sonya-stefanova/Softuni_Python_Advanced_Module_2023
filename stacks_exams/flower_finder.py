from collections import deque

vowels = deque(input().split(" "))  # first
consonants = deque(input().split(" "))  # last

flowers = {
    "rose": list("rose"),
    "tulip": list("tulip"),
    "lotus": list("lotus"),
    "daffodil": list("daffodil")
}
found_word = ""
found = False

while vowels and consonants:
    curr_vowel = vowels.popleft()
    curr_consonant = consonants.pop()

    for k, v in flowers.items():
        if curr_vowel in v:
            counter = v.count(curr_vowel)
            for i in range(counter):
                v.remove(curr_vowel)
        if curr_consonant in v:
            counter = v.count(curr_consonant)
            for i in range(counter):
                v.remove(curr_consonant)

        if len(v)==0:
            found_word = k
            found = True
            break
    if found:
        break

if found:
    print(f'Word found: {found_word}')
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join([str(v) for v in vowels])}")
if consonants:
    print(f"Consonants left: {' '.join([str(c) for c in consonants])}")