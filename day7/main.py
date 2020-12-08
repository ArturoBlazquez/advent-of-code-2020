from utils import read_file, print_part_1, print_part_2, contains_any


def parse_bags():
    bag_lines = read_file('input.txt')

    bags = {}
    for bag_line in bag_lines:
        bag_text, bag_content_text = bag_line.split(' contain ')

        bag = bag_text.replace(' bags', '')
        content = {}
        for bag_content in bag_content_text.replace('.', '').split(', '):
            quantity, *rest = bag_content.split(' ')

            if quantity.isnumeric():
                content[rest[0] + ' ' + rest[1]] = quantity

        bags[bag] = content

    return bags


bags = parse_bags()

# -- PART 1 -- #
bags_that_can_contain_shiny_gold = set()
prev_len = 0

for bag, content in bags.items():
    if 'shiny gold' in content:
        bags_that_can_contain_shiny_gold.add(bag)

while len(bags_that_can_contain_shiny_gold) != prev_len:
    prev_len = len(bags_that_can_contain_shiny_gold)

    for bag, content in bags.items():
        if contains_any(content, bags_that_can_contain_shiny_gold):
            bags_that_can_contain_shiny_gold.add(bag)

print_part_1(len(bags_that_can_contain_shiny_gold))


# -- PART 2 -- #
def get_num_inside_bags(content):
    if content == {}:
        return 0
    else:
        num_inside_bags = 0
        for bag, quantity in content.items():
            num_inside_bags += int(quantity) + int(quantity) * get_num_inside_bags(bags[bag])

        return num_inside_bags


print_part_2(get_num_inside_bags(bags['shiny gold']))
