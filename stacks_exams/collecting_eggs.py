from _collections import deque

eggs_sizes = deque(int(x) for x in input().split(", ")) #take first
paper_size = deque([int(x) for x in input().split(", ")]) #take last
BOX_SIZE = 50
boxes = []

while eggs_sizes and paper_size:

    egg = eggs_sizes.popleft()
    paper = paper_size.pop()

    if egg<=0:
        paper_size.append(paper)
        continue

    if egg==13:
        paper_size.append(paper)
        paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0]
        continue

    total = egg+paper
    if total<=BOX_SIZE:
        boxes.append(total)

if boxes:
    print(f"Great! You filled {len(boxes)} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs_sizes:
    print(f'Eggs left: {", ".join([str(e) for e in eggs_sizes])}')

if paper_size:
    print(f'Pieces of paper left: {", ".join([str(p) for p in paper_size])}')