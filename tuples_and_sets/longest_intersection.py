n = int(input())
longest_intersection = set()

for _ in range(n):
    range_1, range_2 = input().split('-')

    first_start, first_end = [int(x) for x in range_1.split(',')]
    second_start, second_end = [int(x) for x in range_2.split(',')]

    first_output = set(range(first_start, first_end + 1))
    second_output = set(range(second_start, second_end + 1))

    current_intersection = first_output.intersection(second_output)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f'Longest intersection is [{", ".join([str(x) for x in longest_intersection])}] \
with length {len(longest_intersection)}')