rows, cols = [int(x) for x in input().split()]
word = input()

index = 0
for row in range(rows):
    row_elements = [None]*cols

    if row % 2 == 0:
        for col in range(cols):
         #0 is even number
            row_elements[col] = word[index % len(word)]
            index+=1
    else:
        for col in range(cols-1, -1, -1):
            row_elements[col] = word[index % len(word)]
            index += 1
    print(*row_elements, sep='')

