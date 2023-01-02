# #-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
# 	-2.5 - 3 times
# 4.0 - 2 times
# 3.0 - 4 times
# -5.5 - 1 times

nums = (float(x) for x in input().split())
occurances = {}

for num in nums:
    if num not in occurances:
        occurances[num] = 0
    occurances[num] += 1

for kvp in occurances.items():
    print(f'{kvp[0]} - {kvp[1]} times')