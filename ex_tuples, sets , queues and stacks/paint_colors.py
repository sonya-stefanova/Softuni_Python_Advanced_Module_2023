from collections import deque

words = deque(input().split())

main_colours = {"red", "yellow", "blue"}
secondary_colours = {"orange", "purple", "green"}

collected_colours = []

while words:
    left_word = words.popleft()
    right_word = words.pop() if words else ''

    final_colours = left_word + right_word
    if final_colours in main_colours or final_colours in secondary_colours:
        collected_colours.append(final_colours)
        continue

    final_colours = right_word + left_word
    if final_colours in main_colours or final_colours in secondary_colours:
        collected_colours.append(final_colours)
        continue

    left_word = left_word[:-1]
    right_word = right_word[:-1]

    if left_word:
        words.insert(len(words) // 2, left_word)
    if right_word:
        words.insert(len(words) // 2, right_word)

final_colours = []

forming_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

for colour in collected_colours:
    if colour in main_colours:
        final_colours.append(colour)
        continue

    is_collected = True
    for helper_color in forming_colors[colour]:
        if helper_color not in collected_colours:
            is_collected = False
            break

    if is_collected:
        final_colours.append(colour)


# for index, colour in enumerate(collected_colours):
#     if colour in secondary_colours:
#         if secondary_colours[colour][0] not in collected_colours or secondary_colours[colour][1] not in collected_colours:
#             collected_colours.remove(colour)

print(final_colours)