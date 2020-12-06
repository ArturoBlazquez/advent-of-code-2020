from utils import read_file, print_part_1, print_part_2

numList = [int(line) for line in read_file('input.txt')]

# -- PART 1 -- #
for i in range(len(numList)):
    for j in range(i, len(numList)):
        if numList[i] + numList[j] == 2020:
            print_part_1(numList[i] * numList[j])

# -- PART 2 -- #
for i in range(len(numList)):
    for j in range(i, len(numList)):
        for k in range(j, len(numList)):
            if numList[i] + numList[j] + numList[k] == 2020:
                print_part_2(numList[i] * numList[j] * numList[k])
