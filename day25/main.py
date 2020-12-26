from utils import read_file, print_part_1, print_part_2

# -- PARSE INPUT -- #
card_public_key, door_public_key = [int(x) for x in read_file('input.txt')]


# -- PART 1 -- #
def loop(value, subject_number):
    return (value * subject_number) % 20201227


card_value = 1
for card_loop_size in range(1, 100000000):
    card_value = loop(card_value, 7)
    if card_value == card_public_key:
        break

door_value = 1
for door_loop_size in range(1, 100000000):
    door_value = loop(door_value, 7)
    if door_value == door_public_key:
        break

print(card_loop_size, door_loop_size)

encryption_key = 1
for _ in range(card_loop_size):
    encryption_key = loop(encryption_key, door_public_key)

print_part_1(encryption_key)


# -- PART 2 -- #
print_part_2('Merry Xmas')
