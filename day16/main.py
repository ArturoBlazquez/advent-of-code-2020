import numpy as np

from utils import read_file, print_part_1, print_part_2


# -- PARSE INPUT -- #
def parse_input():
    fields = {}
    your_ticket = []
    nearby_tickets = []

    input = read_file('input.txt')
    fields_end = input.index('')

    for field_text in input[:fields_end]:
        field, ranges = field_text.split(': ')
        ranges = [[int(x) for x in range.split('-')] for range in ranges.split(' or ')]

        fields[field] = ranges

    your_ticket = [int(x) for x in input[fields_end + 2].split(',')]

    for ticket_text in input[fields_end + 5:]:
        nearby_tickets.append([int(x) for x in ticket_text.split(',')])

    return fields, your_ticket, nearby_tickets


fields, your_ticket, nearby_tickets = parse_input()

# -- PART 1 -- #
valid_values = []
for field_ranges in fields.values():
    valid_values += list(range(field_ranges[0][0], field_ranges[0][1] + 1))
    valid_values += list(range(field_ranges[1][0], field_ranges[1][1] + 1))

valid_values = set(valid_values)

ticket_scanning_error_rate = 0
for ticket in nearby_tickets:
    for ticket_field in ticket:
        if ticket_field not in valid_values:
            ticket_scanning_error_rate += ticket_field
            break

print_part_1(ticket_scanning_error_rate)

# -- PART 2 -- #
valid_tickets = []
for ticket in nearby_tickets:
    if not any(ticket_field not in valid_values for ticket_field in ticket):
        valid_tickets.append(ticket)

valid_tickets = np.array(valid_tickets)

possible_fields = {}
for i in range(len(your_ticket)):
    possible_fields[i] = []
    for field, field_ranges in fields.items():
        valid_values = list(range(field_ranges[0][0], field_ranges[0][1] + 1)) + \
                       list(range(field_ranges[1][0], field_ranges[1][1] + 1))

        if your_ticket[i] in valid_values and all(ticket in valid_values for ticket in valid_tickets[:, i]):
            possible_fields[i].append(field)

real_fields = {}
while len(real_fields) != len(your_ticket):
    for i in possible_fields:
        if len(possible_fields[i]) == 1:
            real_fields[i] = possible_fields[i][0]
            break

    for j in possible_fields:
        if real_fields[i] in possible_fields[j]:
            possible_fields[j].remove(real_fields[i])

result = 1
for index, field in real_fields.items():
    if 'departure' in field:
        result *= your_ticket[index]
        print(your_ticket[index])

print_part_2(result)
