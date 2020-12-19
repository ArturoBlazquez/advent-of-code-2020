import numpy as np

from utils import read_file, print_part_1, print_part_2

initial_layout_text = [line.replace('.', '0').replace('#', '1') for line in read_file('input.txt')]
initial_layout = [[int(letter) for letter in line] for line in initial_layout_text]

# -- PART 1 -- #
cube_width = len(initial_layout_text) + 12
cube_height = 1 + 12
cube_grid = np.zeros((cube_height, cube_width, cube_width), dtype=bool)

cube_grid[6, 6:6 + len(initial_layout_text), 6:6 + len(initial_layout_text)] = initial_layout


def get_next_grid(cube_grid):
    next_grid = np.zeros((cube_height, cube_width, cube_width), dtype=bool)

    for height in range(len(cube_grid)):
        for row in range(len(cube_grid[0])):
            for column in range(len(cube_grid[0, 0])):
                active_neighbours = get_active_neighbours(cube_grid, height, row, column)
                if cube_grid[height, row, column] == 1:
                    if active_neighbours in [2, 3]:
                        next_grid[height, row, column] = 1
                    else:
                        next_grid[height, row, column] = 0
                else:
                    if active_neighbours == 3:
                        next_grid[height, row, column] = 1
                    else:
                        next_grid[height, row, column] = 0

    return next_grid


def get_active_neighbours(cube_grid, height, row, column):
    min_height = max(0, height - 1)
    min_row = max(0, row - 1)
    min_column = max(0, column - 1)

    neighbours = cube_grid[min_height:height + 2, min_row:row + 2, min_column: column + 2]

    return np.sum(neighbours) - cube_grid[height, row, column]


for _ in range(6):
    cube_grid = get_next_grid(cube_grid)

print_part_1(np.sum(cube_grid))

# -- PART 2 -- #
cube_width = len(initial_layout_text) + 12
cube_height = 1 + 12
initial_range_end = 6 + len(initial_layout_text)
cube_grid = np.zeros((cube_height, cube_width, cube_width, cube_width), dtype=bool)

cube_grid[6, 6, 6:initial_range_end, 6:initial_range_end] = initial_layout

def get_next_grid_v2(grid):
    next_grid = np.zeros((cube_height, cube_width, cube_width, cube_width), dtype=bool)

    for height in range(len(grid)):
        for row in range(len(grid[0])):
            for column in range(len(grid[0, 0])):
                for w in range(len(grid[0, 0, 0])):
                    active_neighbours = get_active_neighbours_v2(grid, height, row, column, w)
                    if grid[height, row, column, w] == 1:
                        if active_neighbours in [2, 3]:
                            next_grid[height, row, column, w] = 1
                        else:
                            next_grid[height, row, column, w] = 0
                    else:
                        if active_neighbours == 3:
                            next_grid[height, row, column, w] = 1
                        else:
                            next_grid[height, row, column, w] = 0

    return next_grid


def get_active_neighbours_v2(grid, height, row, column, w):
    min_height = max(0, height - 1)
    min_row = max(0, row - 1)
    min_column = max(0, column - 1)
    min_w = max(0, w - 1)

    neighbours = grid[min_height:height + 2, min_row:row + 2, min_column: column + 2, min_w: w + 2]

    return np.sum(neighbours) - grid[height, row, column, w]


for _ in range(6):
    cube_grid = get_next_grid_v2(cube_grid)

print_part_2(np.sum(cube_grid))
