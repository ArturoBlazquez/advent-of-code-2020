from utils import read_file, print_part_1, print_part_2

map = read_file('input.txt')

# -- PART 1 -- #
numTrees = 0
xPosition = 0
for mapLine in map:
    if mapLine[xPosition % 31] == '#':
        numTrees += 1

    xPosition += 3

print_part_1(numTrees)

# -- PART 2 -- #
answer = 1
for rightMovement in [1, 3, 5, 7]:
    numTrees = 0
    xPosition = 0
    for mapLine in map:
        if mapLine[xPosition % 31] == '#':
            numTrees += 1

        xPosition += rightMovement

    answer *= numTrees

numTrees = 0
xPosition = 0
for lineNum in range(0, len(map), 2):
    if map[lineNum][xPosition % 31] == '#':
        numTrees += 1

    xPosition += 1

answer *= numTrees

print_part_2(answer)
