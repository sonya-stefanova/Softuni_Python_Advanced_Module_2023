import os

text = input()

try:
    num = int(input())
    print(text * num)
except ValueError:

    print("Variable times must be an integer")
absolute_path=os.path.abspath(__file__)
file_path = os.path.dirname(absolute_path)
print_new_dir = os.path.join(file_path, "custom_dir", "added")
print(print_new_dir)