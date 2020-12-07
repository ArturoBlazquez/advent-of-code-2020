from utils import read_file, print_part_1, print_part_2, duplicates

lines = read_file('input.txt')
groups = ' '.join(lines).split('  ')

# -- PART 1 -- #
num_questions = 0
for group in groups:
    num_questions += len(set(group.replace(' ', '')))

print_part_1(num_questions)

# -- PART 2 -- #
num_questions = 0
for group in groups:
    people = group.split(' ')

    repeated = people[0]
    for person in people[1:]:
        repeated = duplicates(repeated + person)

    num_questions += len(repeated)

print_part_2(num_questions)
