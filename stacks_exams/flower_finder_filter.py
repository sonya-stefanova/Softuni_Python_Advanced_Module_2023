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

    for k in flowers.keys():
        res_1 = list(filter((curr_vowel).__ne__, flowers[k]))  #res_1=[i for i in flowers[k] if i!=curr_vowel]
        flowers[k]=res_1
        res_2 = list(filter((curr_consonant).__ne__, flowers[k]))#res_2=[i for i in flowers[k] if i!=curr_consonant]
        flowers[k]=res_2

        if len(flowers[k]) == 0:
            found = True
            found_word = k
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