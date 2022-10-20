from collections import deque

'''
George Peter Michael William Thomas
3
  1     2     3
George Peter William Thomas
  3            1        2
Peter William Thomas
  1      2      3
Peter William
  1      2
  3
William
'''

kids_string = input()
tosses_count_string = input()

kids_queue = deque(kids_string.split(' '))
tosses_count = int(tosses_count_string)

i = 0
while len(kids_queue) > 1:
    i += 1

    kid = kids_queue.popleft()

    if i < tosses_count:
        kids_queue.append(kid)
    else:
        print(f'Removed {kid}')
        i = 0

print(f'Last is {kids_queue.popleft()}')
