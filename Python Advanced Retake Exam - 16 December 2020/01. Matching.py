from collections import deque


def check_if_zero(value):
    return True if value <= 0 else False


males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches_count = 0

while males and females:
    current_female = females.popleft()
    if check_if_zero(current_female):
        continue
    current_male = males.pop()
    if check_if_zero(current_male):
        females.appendleft(current_female)
        continue

    if current_male % 25 == 0 and males:
        males.pop()
        females.appendleft(current_female)
        continue
    if current_female % 25 == 0 and females:
        females.popleft()
        males.append(current_male)
        continue

    if current_male == current_female:
        matches_count += 1
    else:
        current_male -= 2
        males.append(current_male)
males.reverse()

print(f"Matches: {matches_count}")
if males:
    print(f"Males left: {', '.join(str(x) for x in males)}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print(f"Females left: none")