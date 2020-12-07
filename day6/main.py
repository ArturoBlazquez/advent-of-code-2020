from utils import read_file, print_part_1, print_part_2

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
    for option_chosen_first_person in people[0]:
        flag = True
        for options_chosen_rest in people[1:]:
            if option_chosen_first_person not in options_chosen_rest:
                flag = False
        if flag:
            num_questions += 1

print_part_2(num_questions)
