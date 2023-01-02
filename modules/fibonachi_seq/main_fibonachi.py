from fibonachi_calc import *

def locate_fibonacci_numbers():
    commands = input()
    while commands != "Stop":
        action_info = commands.split(" ")
        command = action_info[0]


        if command == "Create":
            num = int(action_info[2])
            print(" ".join(str(x) for x in create_sequence(num)))

        elif command == "Locate":
            num = int(action_info[1])
            print(locate(num))
        commands = input()

locate_fibonacci_numbers()