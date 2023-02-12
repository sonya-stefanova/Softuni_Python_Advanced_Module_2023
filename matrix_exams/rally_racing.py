def next_post_calc(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1

size = int(input())
racing_number = input()
race_route_matrix = []
tunnel_coordinates = []
car_row, car_col = 0,0
distance_covered = 0

for row in range(size):
    row_elements = input().split()
    race_route_matrix.append(row_elements)

    for col in range(size):
        if "T" in row_elements[col]:
            tunnel_coordinates.append([row, col])

race_route_matrix[car_row][car_col] = "."

direction = input()
while True:
    if direction == "End":
        race_route_matrix[car_row][car_col] = "C"
        print(f"Racing car {racing_number} DNF.")
        break

    car_row, car_col = next_post_calc(direction, car_row, car_col)
    sign = race_route_matrix[car_row][car_col]

    if race_route_matrix[car_row][car_col] == "F":
        distance_covered+=10
        race_route_matrix[car_row][car_col] = "C"
        print(f"Racing car {racing_number} finished the stage!")
        break

    elif race_route_matrix[car_row][car_col] == "T":
        race_route_matrix[car_row][car_col] = "."
        tunnel_coord = [car_row, car_col]
        for el in tunnel_coordinates:
            tunnel_coordinates.remove(tunnel_coord)
        car_row, car_col = tunnel_coordinates[0]
        distance_covered+=30

    else:
        distance_covered+=10

    race_route_matrix[car_row][car_col] = "."
    direction = input()

print(f"Distance covered {distance_covered} km." )
[print(*row, sep = "") for row in race_route_matrix]
