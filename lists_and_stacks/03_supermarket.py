from collections import deque
'''
To DO:
1) create an empty queue
2) loop:
    add each input to the queue
    if input is 'Paid':
        print the queue and empty it
        
3)print remaining after receiving the command "End"
'''

queue = deque()
command = input()

while command != "End":
    people = command

    if people == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(people)

    command = input()


print(f'{len(queue)} people remaining.')
