from utils import read_file, print_part_1, print_part_2, replace_index


def parse_program():
    program_lines = []
    for line in read_file('input.txt'):
        instruction, value = line.split(' = ')

        if instruction == 'mask':
            program_lines.append({instruction: value})
        else:
            instruction = instruction.replace('mem[', '').replace(']', '')
            program_lines.append({int(instruction): int(value)})

    return program_lines


program_lines = parse_program()


# -- PART 1 -- #
def apply_mask(mask, number):
    mask_for_or = int(mask.replace('X', '0'), 2)
    mask_for_and = int(mask.replace('X', '1'), 2)

    return (number | mask_for_or) & mask_for_and


mask = ''
memory = {}
for program_line in program_lines:
    instruction, value = list(program_line.items())[0]

    if instruction == 'mask':
        mask = value
    else:
        memory[instruction] = apply_mask(mask, value)

print_part_1(sum(memory.values()))


# -- PART 2 -- #
def apply_mask_v2(mask, number):
    mask_for_or = int(mask.replace('X', '0'), 2)

    number_masked_in_binary = bin(number | mask_for_or)[2:].zfill(36)

    for i in range(len(mask)):
        if mask[i] == 'X':
            number_masked_in_binary = replace_index(number_masked_in_binary, i, 'X')

    return number_masked_in_binary


def get_floating_values(number):
    x_position = number.find('X')
    if x_position < 0:
        return [number]
    else:
        replaced_with_zero = get_floating_values(replace_index(number, x_position, '0'))
        replaced_with_one = get_floating_values(replace_index(number, x_position, '1'))

        return replaced_with_zero + replaced_with_one


mask = ''
memory = {}
for program_line in program_lines:
    instruction, value = list(program_line.items())[0]

    if instruction == 'mask':
        mask = value
    else:
        for mem_value in get_floating_values(apply_mask_v2(mask, instruction)):
            memory[mem_value] = value

print_part_2(sum(memory.values()))
