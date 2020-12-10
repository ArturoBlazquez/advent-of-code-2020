from utils import read_file, print_part_1, print_part_2

joltages = [int(line) for line in read_file('input.txt')]
joltages.append(0)
joltages.append(max(joltages) + 3)

# -- PART 1 -- #
joltages.sort()

num_1_jolt_difference = sum([1 for i in range(len(joltages) - 1) if joltages[i + 1] - joltages[i] == 1])
num_3_jolt_difference = sum([1 for i in range(len(joltages) - 1) if joltages[i + 1] - joltages[i] == 3])

print_part_1(num_1_jolt_difference * num_3_jolt_difference)

# -- PART 2 -- #
num_arrangements = {}

for joltage in range(max(joltages) + 1):
    if joltage in joltages:
        if joltage == 0:
            num_arrangements[joltage] = 1
        elif joltage == 1:
            num_arrangements[joltage] = 1
        elif joltage == 2:
            num_arrangements[joltage] = 2
        else:
            num_arrangements[joltage] = num_arrangements[joltage - 1] + num_arrangements[joltage - 2] + \
                                        num_arrangements[joltage - 3]
    else:
        num_arrangements[joltage] = 0

print_part_2(num_arrangements[max(joltages)])
