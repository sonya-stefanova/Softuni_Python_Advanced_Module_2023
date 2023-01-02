n,m = [int(x) for x in input().split()]
set_n = set()
set_m = set()

for _ in range(n):
    set_n.add(int(input()))

for _ in range(m):
    set_m.add(int(input()))

intersection = set_n.intersection(set_m)
for num in intersection:
    print(num)