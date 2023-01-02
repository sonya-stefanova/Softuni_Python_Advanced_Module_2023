# 20, 13, -7, 7
# 10, 5, 20, 15, 7, 9

from collections import deque

eggs = deque([int(egg) for egg in input().split(", ")])
paper = [int(x) for x in input().split(", ")]


box_size = 50
box_counter = 0

while eggs and paper:
    current_egg = eggs.popleft()
    current_paper = paper.pop()
    eggs_and_paper = current_paper+current_egg

    if current_egg <= 0:
        paper.append(current_paper)
        continue

    if current_egg == 13:
        paper.append(current_paper)
        paper[0], paper[-1] = paper[-1], paper[0]
        continue

    if eggs_and_paper <= box_size:
        box_counter+=1


if box_counter>=1:
    print(f"Great! You filled {box_counter} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join([str(x) for x in eggs])}')
if paper:
    print(f'Pieces of paper left: {", ".join([str(x) for x in paper])}')
