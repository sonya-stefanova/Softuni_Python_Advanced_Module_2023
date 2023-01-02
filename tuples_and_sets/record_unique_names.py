number_of_lines = int(input())
unique_names = set()
for _ in range(number_of_lines):
    unique_names.add(input())
print('\n'.join(unique_names))
