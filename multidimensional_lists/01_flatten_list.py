# sublists = input().split("|")
#
# new = []
#
# for i in range(len(sublists)-1, -1, -1):
#     current_elements = sublists[i].strip().split()
#     new.extend(current_elements)
# print(*new, sep = " ")


sublists = input().split("|")

new = []
while sublists:
    current_sublist = sublists.pop().split()

    for el in current_sublist:
        new.append(el)
print(*new, sep = " ")