import numpy as np

from utils import read_file, print_part_1, print_part_2


# -- PARSE INPUT -- #
def parse_input():
    images = {}

    input = read_file('input.txt')

    i = 0
    while i < len(input):
        tile_id = int(input[i][5:9])
        image_text = [line.replace('.', '0').replace('#', '1') for line in input[i + 1:i + 11]]
        image = np.array([[letter for letter in line] for line in image_text])

        top_row_id = int(''.join(image[0, :]), 2)
        bottom_row_id = int(''.join(image[-1, :]), 2)
        left_col_id = int(''.join(image[:, 0]), 2)
        right_col_id = int(''.join(image[:, -1]), 2)

        top_row_id_rot = int(''.join(image[0, :])[::-1], 2)
        bottom_row_id_rot = int(''.join(image[-1, :])[::-1], 2)
        left_col_id_rot = int(''.join(image[:, 0])[::-1], 2)
        right_col_id_rot = int(''.join(image[:, -1])[::-1], 2)

        images[tile_id] = {'image': image, 'ids': [top_row_id, bottom_row_id, left_col_id, right_col_id],
                           'rotated_ids': [top_row_id_rot, bottom_row_id_rot, left_col_id_rot, right_col_id_rot]}

        i += 12

    return images


images = parse_input()

# -- PART 1 -- #
corners = []

img_keys = list(images.keys())

for i in range(len(img_keys)):
    top_value, bottom_value, left_value, right_value = images[img_keys[i]]['ids']

    top_left_is_border = True
    top_right_is_border = True
    bottom_right_is_border = True
    bottom_left_is_border = True

    for j in range(len(img_keys)):
        if i != j:
            second_tile_values = images[img_keys[j]]['ids'] + images[img_keys[j]]['rotated_ids']

            if top_value in second_tile_values or left_value in second_tile_values:
                top_left_is_border = False
            if top_value in second_tile_values or right_value in second_tile_values:
                top_right_is_border = False
            if bottom_value in second_tile_values or right_value in second_tile_values:
                bottom_right_is_border = False
            if bottom_value in second_tile_values or left_value in second_tile_values:
                bottom_left_is_border = False

            if (top_left_is_border is False) and (top_right_is_border is False) and (bottom_right_is_border is False) \
                    and (bottom_left_is_border is False):
                break

    if top_left_is_border or top_right_is_border or bottom_right_is_border or bottom_left_is_border:
        corners.append(img_keys[i])

result = 1
for corner in corners:
    result *= corner

print_part_1(result)


# -- PART 2 -- #
def rotate_to_match_right_side(side_id, tile, tile_values):
    matching_side = tile_values.index(side_id)

    if matching_side == 0:
        tile_image = np.rot90(np.fliplr(tile['image']))
        right_value = tile['ids'][1]
        bottom_value = tile['ids'][3]
    elif matching_side == 1:
        tile_image = np.rot90(tile['image'], 3)
        right_value = tile['ids'][0]
        bottom_value = tile['rotated_ids'][3]
    elif matching_side == 2:
        tile_image = tile['image']
        right_value = tile['ids'][3]
        bottom_value = tile['ids'][1]
    elif matching_side == 3:
        tile_image = np.fliplr(tile['image'])
        right_value = tile['ids'][2]
        bottom_value = tile['rotated_ids'][1]
    elif matching_side == 4:
        tile_image = np.rot90(tile['image'])
        right_value = tile['rotated_ids'][1]
        bottom_value = tile['ids'][2]
    elif matching_side == 5:
        tile_image = np.rot90(np.fliplr(tile['image']), 3)
        right_value = tile['rotated_ids'][0]
        bottom_value = tile['rotated_ids'][2]
    elif matching_side == 6:
        tile_image = np.rot90(np.fliplr(tile['image']), 2)
        right_value = tile['rotated_ids'][3]
        bottom_value = tile['ids'][0]
    else:
        tile_image = np.rot90(tile['image'], 2)
        right_value = tile['rotated_ids'][2]
        bottom_value = tile['rotated_ids'][0]

    return tile_image, right_value, bottom_value


def place_tiles_on_right():
    for _ in range(sea_image_size - 1):
        for image_id in images:
            if image_id not in used_images:
                tile_values = images[image_id]['ids'] + images[image_id]['rotated_ids']

                if sea_image_unparsed[-1]['right_value'] in tile_values:
                    tile_image, right_value, bottom_value = rotate_to_match_right_side(
                        sea_image_unparsed[-1]['right_value'], images[image_id], tile_values)

                    sea_image_unparsed.append({'image_id': image_id, 'image': tile_image,
                                               'right_value': right_value, 'bottom_value': bottom_value})
                    used_images.append(image_id)


def rotate_to_match_bottom_side(side_id, tile, tile_values):
    matching_side = tile_values.index(side_id)

    if matching_side == 0:
        tile_image = tile['image']
        right_value = tile['ids'][3]
        bottom_value = tile['ids'][1]
    elif matching_side == 1:
        tile_image = np.rot90(np.fliplr(tile['image']), 2)
        right_value = tile['rotated_ids'][3]
        bottom_value = tile['ids'][0]
    elif matching_side == 2:
        tile_image = np.rot90(np.fliplr(tile['image']))
        right_value = tile['ids'][1]
        bottom_value = tile['ids'][3]
    elif matching_side == 3:
        tile_image = np.rot90(tile['image'])
        right_value = tile['rotated_ids'][1]
        bottom_value = tile['ids'][2]
    elif matching_side == 4:
        tile_image = np.fliplr(tile['image'])
        right_value = tile['ids'][2]
        bottom_value = tile['rotated_ids'][1]
    elif matching_side == 5:
        tile_image = np.rot90(tile['image'], 2)
        right_value = tile['rotated_ids'][2]
        bottom_value = tile['rotated_ids'][0]
    elif matching_side == 6:
        tile_image = np.rot90(tile['image'], 3)
        right_value = tile['ids'][0]
        bottom_value = tile['rotated_ids'][3]
    else:
        tile_image = np.rot90(np.fliplr(tile['image']), 3)
        right_value = tile['rotated_ids'][0]
        bottom_value = tile['rotated_ids'][2]

    return tile_image, right_value, bottom_value


def place_tile_on_bottom():
    for image_id in images:
        if image_id not in used_images:
            tile_values = images[image_id]['ids'] + images[image_id]['rotated_ids']

            if sea_image_unparsed[-sea_image_size]['bottom_value'] in tile_values:
                tile_image, right_value, bottom_value = rotate_to_match_bottom_side(
                    sea_image_unparsed[-sea_image_size]['bottom_value'], images[image_id], tile_values)

                sea_image_unparsed.append({'image_id': image_id, 'image': tile_image,
                                           'right_value': right_value, 'bottom_value': bottom_value})
                used_images.append(image_id)


sea_image_size = 12
sea_image_unparsed = [{'image_id': corners[0], 'image': images[corners[0]]['image'],
                       'right_value': images[corners[0]]['ids'][3], 'bottom_value': images[corners[0]]['ids'][1]}]
used_images = [corners[0]]

place_tiles_on_right()

for _ in range(sea_image_size - 1):
    place_tile_on_bottom()
    place_tiles_on_right()

sea_image = np.zeros([8 * sea_image_size, 8 * sea_image_size], dtype=str)

for row in range(sea_image_size):
    for col in range(sea_image_size):
        unparsed_index = row * sea_image_size + col
        sea_image[row * 8:row * 8 + 8, col * 8:col * 8 + 8] = sea_image_unparsed[unparsed_index]['image'][1:-1, 1:-1]


def contains_sea_monster(grid):
    monster_places = [grid[0, 18], grid[1, 0],
                      grid[1, 5], grid[1, 6], grid[1, 11], grid[1, 12], grid[1, 17], grid[1, 18], grid[1, 19],
                      grid[2, 1], grid[2, 4], grid[2, 7], grid[2, 10], grid[2, 13], grid[2, 16]]

    if '0' in monster_places:
        return False
    return True


# get appropriate orientation of sea image
num_monsters = 0
while num_monsters == 0:
    sea_image = np.fliplr(sea_image)
    for _ in range(4):
        sea_image = np.rot90(sea_image)

        num_monsters = 0
        for row in range(len(sea_image) - 3):
            for col in range(len(sea_image) - 20):
                if contains_sea_monster(sea_image[row:row + 3, col:col + 20]):
                    num_monsters += 1

        if num_monsters != 0:
            break


def add_marks(grid):
    grid[0, 18] = 'x'
    grid[1, 0] = 'x'
    grid[1, 5] = 'x'
    grid[1, 6] = 'x'
    grid[1, 11] = 'x'
    grid[1, 12] = 'x'
    grid[1, 17] = 'x'
    grid[1, 18] = 'x'
    grid[1, 19] = 'x'
    grid[2, 1] = 'x'
    grid[2, 4] = 'x'
    grid[2, 7] = 'x'
    grid[2, 10] = 'x'
    grid[2, 13] = 'x'
    grid[2, 16] = 'x'


for row in range(len(sea_image) - 3):
    for col in range(len(sea_image) - 20):
        if contains_sea_monster(sea_image[row:row + 3, col:col + 20]):
            add_marks(sea_image[row:row + 3, col:col + 20])

print_part_2(np.count_nonzero(sea_image == '1'))
