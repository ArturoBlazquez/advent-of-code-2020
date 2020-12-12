from utils import read_file, print_part_1, matrix_are_equal, print_part_2

seat_layout = read_file('input.txt')


# -- PART 1 -- #
def get_next_layout(layout):
    next_layout = []

    for row in range(len(layout)):
        next_row = ''
        for column in range(len(layout[0])):
            seat = layout[row][column]
            if seat == '.':
                next_row += '.'
            elif seat == 'L':
                neighbours = get_neighbours(layout, row, column)
                if '#' not in neighbours:
                    next_row += '#'
                else:
                    next_row += 'L'
            else:
                neighbours = get_neighbours(layout, row, column)
                if neighbours.count('#') >= 4:
                    next_row += 'L'
                else:
                    next_row += '#'

        next_layout.append(next_row)

    return next_layout


def get_neighbours(layout, row, column):
    max_row = len(layout) - 1
    max_column = len(layout[0]) - 1
    neighbours = []

    if row > 0:
        neighbours.append(layout[row - 1][column])
        if column > 0:
            neighbours.append(layout[row - 1][column - 1])
        if column < max_column:
            neighbours.append(layout[row - 1][column + 1])
    if row < max_row:
        neighbours.append(layout[row + 1][column])
        if column > 0:
            neighbours.append(layout[row + 1][column - 1])
        if column < max_column:
            neighbours.append(layout[row + 1][column + 1])
    if column > 0:
        neighbours.append(layout[row][column - 1])
    if column < max_column:
        neighbours.append(layout[row][column + 1])

    return neighbours


next_layout = get_next_layout(seat_layout)

while not matrix_are_equal(next_layout, seat_layout):
    seat_layout = next_layout
    next_layout = get_next_layout(seat_layout)

print_part_1(sum([row.count('#') for row in seat_layout]))


# -- PART 2 -- #
def get_next_layout_v2(layout):
    next_layout = []

    for row in range(len(layout)):
        next_row = ''
        for column in range(len(layout[0])):
            seat = layout[row][column]
            if seat == '.':
                next_row += '.'
            elif seat == 'L':
                neighbours = get_neighbours_v2(layout, row, column)
                if '#' not in neighbours:
                    next_row += '#'
                else:
                    next_row += 'L'
            else:
                neighbours = get_neighbours_v2(layout, row, column)
                if neighbours.count('#') >= 5:
                    next_row += 'L'
                else:
                    next_row += '#'

        next_layout.append(next_row)

    return next_layout


def get_neighbours_v2(layout, row, column):
    max_row = len(layout) - 1
    max_column = len(layout[0]) - 1
    neighbours = []

    seats_up = row
    seats_down = max_row - row
    seats_left = column
    seats_right = max_column - column

    for i in range(1, min(seats_up, seats_left) + 1):
        if layout[row - i][column - i] != '.':
            neighbours.append(layout[row - i][column - i])
            break

    for i in range(1, seats_up + 1):
        if layout[row - i][column] != '.':
            neighbours.append(layout[row - i][column])
            break

    for i in range(1, min(seats_up, seats_right) + 1):
        if layout[row - i][column + i] != '.':
            neighbours.append(layout[row - i][column + i])
            break

    for i in range(1, seats_left + 1):
        if layout[row][column - i] != '.':
            neighbours.append(layout[row][column - i])
            break

    for i in range(1, seats_right + 1):
        if layout[row][column + i] != '.':
            neighbours.append(layout[row][column + i])
            break

    for i in range(1, min(seats_down, seats_left) + 1):
        if layout[row + i][column - i] != '.':
            neighbours.append(layout[row + i][column - i])
            break

    for i in range(1, seats_down + 1):
        if layout[row + i][column] != '.':
            neighbours.append(layout[row + i][column])
            break

    for i in range(1, min(seats_down, seats_right) + 1):
        if layout[row + i][column + i] != '.':
            neighbours.append(layout[row + i][column + i])
            break

    return neighbours


seat_layout = read_file('input.txt')
next_layout = get_next_layout_v2(seat_layout)

while not matrix_are_equal(next_layout, seat_layout):
    seat_layout = next_layout
    next_layout = get_next_layout_v2(seat_layout)

print_part_2(sum([row.count('#') for row in seat_layout]))
