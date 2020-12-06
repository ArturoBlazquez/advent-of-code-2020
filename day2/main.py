from operator import xor

from utils import read_file, print_part_1, print_part_2

lines = read_file('input.txt')

# -- PART 1 -- #
numValidPasswords = 0
for line in lines:
    policy, password = line.split(': ')
    times, letter = policy.split(' ')
    minTimes, maxTimes = times.split('-')

    minTimes = int(minTimes)
    maxTimes = int(maxTimes)

    if password.count(letter) in range(minTimes, maxTimes + 1):
        numValidPasswords += 1

print_part_1(numValidPasswords)

# -- PART 2 -- #
numValidPasswords = 0
for line in lines:
    policy, password = line.split(': ')
    times, letter = policy.split(' ')
    firstPosition, secondPosition = times.split('-')

    firstPosition = int(firstPosition) - 1
    secondPosition = int(secondPosition) - 1

    if xor(password[firstPosition] == letter, password[secondPosition] == letter):
        numValidPasswords += 1

print_part_2(numValidPasswords)
