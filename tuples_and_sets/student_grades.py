num = int(input())
students = {}

for _ in range(num):
    name, grade = input().split()
    grade = float(grade)
    if name not in students:
        students[name] = []
    students[name].append(grade)

for kvp in students.items():
    print(f'{kvp[0]} -> {" ".join([f"{el:.2f}" for el in kvp[1]])} (avg: {(sum(kvp[1]) / len(kvp[1])):.2f})')