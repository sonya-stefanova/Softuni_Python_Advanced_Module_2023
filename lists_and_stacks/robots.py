from collections import deque

#ROB-15;SS2-10;NX8000-3
# 8:00:00
# detail
# glass
# wood
# apple
# End

def robots_dictionary():
    robot_dict = {}
    robots_input = input().split(";") #get list of robots with their time [ROB-15;SS2-10;NX8000-3]
    #then, loop through each robot with time by splitting by "-" to get the name and the time individually
    for robot in robots_input:
        robot_details = robot.split("-")
        name = robot_details[0]
        processing_time = int(robot_details[1])
        robot_dict[name] = processing_time #add them in a dictionary
    return robot_dict


def read_products():
    '''This function reads the items and add them into a queue.'''
    products_queue = deque()
    while True:
        command = input()
        if command == 'End':
            break
        products_queue.append(command)
    return products_queue


def convert_to_seconds(hours, minutes, seconds):
    return hours * 60 * 60 + minutes * 60 + seconds


def convert_to_hours(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots = robots_dictionary() #read the dictionary

available_robots = [robot for robot in robots.keys()]
processing_robots = {}
starting_time = [int(x) for x in input().split(":")]
time_seconds = convert_to_seconds(starting_time[0], starting_time[1], starting_time[2])

products = read_products()

while products:
    time_seconds = (time_seconds + 1) % (24 * 60 * 60)
    for robot_name in [robot for robot in processing_robots.keys()]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] <= 0:
            processing_robots.pop(robot_name)

    current_product = products.popleft()
    for robot_name in available_robots:
        if robot_name not in processing_robots:
            processing_robots[robot_name] = robots[robot_name]
            print(f'{robot_name} - {current_product} [{convert_to_hours(time_seconds)}]')
            break
    else:
        products.append(current_product)
