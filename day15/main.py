from utils import read_file, print_part_1, print_part_2

starting_numbers = [int(x) for x in read_file('input.txt')[0].split(',')]

# -- PART 1 -- #
previous_said_number = starting_numbers[-1]
spoken_nums = {}

for index, number in enumerate(starting_numbers, start=1):
    spoken_nums[number] = [index, index]

for turn in range(len(starting_numbers) + 1, 2021):
    current_said_num = spoken_nums[previous_said_number][-1] - spoken_nums[previous_said_number][-2]

    previous_said_number = current_said_num

    if current_said_num in spoken_nums:
        spoken_nums[current_said_num].append(turn)
    else:
        spoken_nums[current_said_num] = [turn, turn]

print_part_1(previous_said_number)

# -- PART 2 -- #
for turn in range(2021, 30000001):
    current_said_num = spoken_nums[previous_said_number][-1] - spoken_nums[previous_said_number][-2]

    previous_said_number = current_said_num

    if current_said_num in spoken_nums:
        spoken_nums[current_said_num].append(turn)
    else:
        spoken_nums[current_said_num] = [turn, turn]

print_part_2(previous_said_number)
