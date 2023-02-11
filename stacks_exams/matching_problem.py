from collections import deque


def check_if_zero(value):
    return True if value <= 0 else False


males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0
while males and females:
    m = males.pop()
    if m<=0:
        continue

    f = females.popleft()
    if f <=0:
        males.append(m)
        continue

    if m%25==0:
        males.pop()
        females.appendleft(f)
        continue

    if f%25==0:
        females.popleft()
        males.append(m)
        continue

    if m!=f:
        m-=2
        males.append(m)
    else:
        matches+=1

males = males[::-1]
print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(x) for x in males)}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print(f"Females left: none")