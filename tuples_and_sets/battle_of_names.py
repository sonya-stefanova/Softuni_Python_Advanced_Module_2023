
n = int(input())

even = set()
odd = set()

for row in range(1, n + 1):
    current_name = input()
    ascii_sum_name = sum([ord(x) for x in current_name]) // row
    if ascii_sum_name % 2 == 0:
        even.add(ascii_sum_name)
    else:
        odd.add(ascii_sum_name)

even_sum = sum(even)
odd_sum = sum(odd)

if even_sum == odd_sum:
    output = odd.union(even)
elif even_sum > odd_sum:
    output = odd.symmetric_difference(even)
else:
    output = odd.difference(even)

print(*output, sep=', ')