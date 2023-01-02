lines = int(input())
set = set()
for _ in range(lines):
    row = input().split()
    for el in row:
        set.add(el)

for unique_element in set:
    print(unique_element)


# n = int(input())
#
# output = set()
#
# for _ in range(n):
#     current_set = set(input().split())
#     output = output.union(current_set)
#
# for el in output:
#     print(el)