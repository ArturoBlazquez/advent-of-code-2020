from utils import read_file, print_part_1, print_part_2

# -- PARSE INPUT -- #
flipping_list = read_file('input.txt')


# -- PART 1 -- #
def get_coordinates(direction):
    x = 0
    y = 0

    while direction != '':
        if direction[0] == 'e':
            x += 1
            direction = direction[1:]
        elif direction[0] == 'w':
            x -= 1
            direction = direction[1:]
        else:
            if direction[0:2] == 'se':
                y -= 1
            elif direction[0:2] == 'sw':
                x -= 1
                y -= 1
            elif direction[0:2] == 'nw':
                y += 1
            else:
                x += 1
                y += 1
            direction = direction[2:]

    return x, y


tiles = {}
for flip in flipping_list:
    coord = get_coordinates(flip)

    if coord in tiles:
        tiles[coord] = (tiles[coord] + 1) % 2
    else:
        tiles[coord] = 1

print_part_1(sum(tiles.values()))


# -- PART 2 -- #
def get_num_black_neighbours(position):
    x, y = position
    return sum(
        [tiles[x, y + 1], tiles[x + 1, y + 1], tiles[x - 1, y], tiles[x + 1, y], tiles[x - 1, y - 1], tiles[x, y - 1]])


def get_next_tiles(tiles):
    next_tiles = tiles.copy()

    for x in range(-max_index - 104, -max_index + 104):
        for y in range(-max_index - 104, -max_index + 104):
            num_black_neighbours = get_num_black_neighbours((x, y))

            if tiles[(x, y)] == 1:
                if num_black_neighbours == 0 or num_black_neighbours > 2:
                    next_tiles[(x, y)] = 0
            else:
                if num_black_neighbours == 2:
                    next_tiles[(x, y)] = 1

    return next_tiles


max_index = max([max(abs(x), abs(y)) for x, y in tiles])

for i in range(-max_index - 105, -max_index + 105):
    for j in range(-max_index - 105, -max_index + 105):
        if (i, j) not in tiles:
            tiles[i, j] = 0

for _ in range(100):
    tiles = get_next_tiles(tiles)

print_part_2(sum(tiles.values()))
