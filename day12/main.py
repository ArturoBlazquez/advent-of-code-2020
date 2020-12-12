from utils import read_file, print_part_1, print_part_2

instructions = [[instruction[0], int(instruction[1:])] for instruction in read_file('input.txt')]

# -- PART 1 -- #
directions = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}
steps_north = 0
steps_east = 0
facing = 1

for instruction in instructions:
    action, value = instruction

    if action == 'N':
        steps_north += value
    elif action == 'S':
        steps_north -= value
    elif action == 'E':
        steps_east += value
    elif action == 'W':
        steps_east -= value

    elif action == 'L':
        facing = (facing - value // 90) % 4
    elif action == 'R':
        facing = (facing + value // 90) % 4
    else:
        if directions[facing] == 'N':
            steps_north += value
        elif directions[facing] == 'S':
            steps_north -= value
        elif directions[facing] == 'E':
            steps_east += value
        elif directions[facing] == 'W':
            steps_east -= value

print_part_1(abs(steps_north) + abs(steps_east))

# -- PART 2 -- #
steps_north = 0
steps_east = 0
waypoint_north = 1
waypoint_east = 10

for instruction in instructions:
    action, value = instruction

    if action == 'F':
        steps_north += waypoint_north * value
        steps_east += waypoint_east * value

    elif action == 'N':
        waypoint_north += value
    elif action == 'S':
        waypoint_north -= value
    elif action == 'E':
        waypoint_east += value
    elif action == 'W':
        waypoint_east -= value

    else:
        if value // 90 == 2:  # rotate 180º
            waypoint_north, waypoint_east = -waypoint_north, -waypoint_east
        if (action == 'L' and value // 90 == 1) or (action == 'R' and value // 90 == 3):  # rotate right
            waypoint_north, waypoint_east = waypoint_east, -waypoint_north
        if (action == 'L' and value // 90 == 3) or (action == 'R' and value // 90 == 1):  # rotate left
            waypoint_north, waypoint_east = -waypoint_east, waypoint_north

print_part_2(abs(steps_north) + abs(steps_east))
