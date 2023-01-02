# rows, cols = [int(x) for x in input().split()]
#
# alphabet = {
#     0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm',
#     13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y',
#     25: 'z'
#             }
#
# for row in range(rows):
#     for col in range(cols):
#         el = alphabet[row] + alphabet[col + row] + alphabet[row]
#         print(el, end=' ')
#     print()


# 2nd decision
# rows, cols = [int(x) for x in input().split()]
#
# alph = 'abcdefghijklmnopqrstuvwxyz'
#
# for i in range(rows):
#     row = [f'{alph[i]}{alph[j]}{alph[i]}' for j in range(i, cols + i)]
#     print (*row, sep=' ')

# 05. Matrix of Palindromes:
r, c = [int(z) for z in input().split()]
matrix = []
for row in range(r):
    for col in range(c):
        print(f'{chr(row + 97)}{chr(col+ row + 97)}{chr(row + 97)}', end = " ")
    print()
