from utils import read_file, print_part_1, print_part_2


# -- PARSE INPUT -- #
def parse_input():
    rules = {}
    messages = []

    input = read_file('input.txt')
    rules_end = input.index('')

    for field_text in input[:rules_end]:
        rule, matching = field_text.split(': ')

        rule = int(rule)

        if '"' in matching:
            rules[rule] = matching[1]
        elif '|' in matching:
            rules[rule] = [[int(x) for x in match.split(' ')] for match in matching.split(' | ')]
        else:
            rules[rule] = [int(x) for x in matching.split(' ')]

    messages = input[rules_end + 1:]

    return rules, messages


rules, messages = parse_input()

# -- PART 1 -- #
calculated_messages = {}


def combine_lists(list1, list2):
    return [string1 + string2 for string1 in list1 for string2 in list2]


def get_valid_messages(rule_index):
    if rule_index in calculated_messages:
        return calculated_messages[rule_index]

    rule = rules[rule_index]

    if isinstance(rule, str):
        calculated_messages[rule_index] = [rule]
    elif isinstance(rule[0], int):
        if len(rule) == 1:
            calculated_messages[rule_index] = get_valid_messages(rule[0])
        else:
            calculated_messages[rule_index] = combine_lists(get_valid_messages(rule[0]), get_valid_messages(rule[1]))
    else:
        if len(rule[0]) == 1:
            calculated_messages[rule_index] = get_valid_messages(rule[0][0]) + get_valid_messages(rule[1][0])
        else:
            first_messages = combine_lists(get_valid_messages(rule[0][0]), get_valid_messages(rule[0][1]))
            second_messages = combine_lists(get_valid_messages(rule[1][0]), get_valid_messages(rule[1][1]))
            calculated_messages[rule_index] = first_messages + second_messages

    return get_valid_messages(rule_index)


valid_messages = get_valid_messages(0)

num_valid_messages = 0
for message in messages:
    if message in valid_messages:
        num_valid_messages += 1

print_part_1(num_valid_messages)

# -- PART 2 -- #
valid_message_42 = calculated_messages[42]
valid_message_31 = calculated_messages[31]


def substring_is_valid(substring):
    num_42s = 0
    for i in range(0, len(substring), 8):
        if substring[i:i + 8] not in valid_message_42:
            break
        else:
            num_42s += 1

    num_31s = 0
    for i in range(len(substring) - 8, -1, -8):
        if substring[i:i + 8] not in valid_message_31:
            break
        else:
            num_31s += 1

    if (num_42s + num_31s) * 8 >= len(substring) and num_42s * 8 * 2 >= len(substring):
        return True
    else:
        return False


num_valid_messages = 0
for message in messages:
    if message[0:8] in valid_message_42 and message[8:16] in valid_message_42:
        if message[-8:] in valid_message_31:
            if substring_is_valid(message[16:-8]):
                num_valid_messages += 1

print_part_2(num_valid_messages)
