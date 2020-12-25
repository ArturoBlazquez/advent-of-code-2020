import numpy as np

from utils import read_file, print_part_1, print_part_2

# -- PARSE INPUT -- #
cups = [int(letter) for letter in read_file('input.txt')[0]]


# -- PART 1 -- #
def move(cups_list):
    current_cup = cups_list[0]
    three_cups = cups_list[1:4]
    other_cups = cups_list[4:]

    cut_position = 0
    for i in range(1, 5):
        index_to_find = ((current_cup - 1 - i) % 9) + 1
        if index_to_find in other_cups:
            cut_position = other_cups.index(index_to_find) + 1
            break

    return other_cups[:cut_position] + three_cups + other_cups[cut_position:] + [current_cup]


for _ in range(100):
    cups = move(cups)

one_position = cups.index(1)
print_part_1(''.join([str(x) for x in cups[one_position + 1:] + cups[:one_position]]))


# -- PART 2 -- #
def move_v2(cups_list):
    current_cup = np.where(cups_list == 0)[0][0]
    three_cups = [np.where(cups_list == 1)[0][0], np.where(cups_list == 2)[0][0], np.where(cups_list == 3)[0][0]]

    for i in range(1, 5):
        index_to_find = (current_cup - i) % 9
        if index_to_find in three_cups:
            pass
        else:
            cut = cups_list[index_to_find]
            break

    cups_list[np.where(cups_list > cut)[0]] += 3
    cups_list -= 4
    cups_list[current_cup] = 8
    cups_list[three_cups[0]] = cut - 3
    cups_list[three_cups[1]] = cut - 2
    cups_list[three_cups[2]] = cut - 1


cups_unparsed = [int(letter) for letter in read_file('input.txt')[0]]
cups = []
for i in range(1, 10):
    cups.append(cups_unparsed.index(i))
cups = np.array(cups + list(range(9, 1000000)))


def print_list(cups_list):
    for i in range(len(cups_list)):
        print(np.where(cups_list == i)[0][0] + 1, end=' ')

    print('')


for _ in range(10000):
    move_v2(cups)

# one_position = cups.index(1)
# print(one_position)
# print(cups[one_position + 1])
# print(cups[one_position + 2])

print_part_2(cups)
