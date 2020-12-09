from utils import read_file, print_part_1, print_part_2, contains_any

instructions = read_file('input.txt')

# -- PART 1 -- #
runt_instructions = []
acc = 0
current_instruction = 0

while current_instruction not in runt_instructions:
    runt_instructions.append(current_instruction)

    instruction = instructions[current_instruction]
    operation, argument = instruction.split(' ')
    argument = int(argument)

    if operation == 'acc':
        acc += argument
        current_instruction += 1
    elif operation == 'jmp':
        current_instruction += argument
    else:
        current_instruction += 1

print_part_1(acc)

# -- PART 2 -- #
instructions_with_nop_or_jmp = []
for i in range(len(instructions)):
    if contains_any(instructions[i], ['jmp', 'nop']):
        instructions_with_nop_or_jmp.append(i)

for instruction_to_change in instructions_with_nop_or_jmp:
    instructions_modified = instructions.copy()
    if 'jmp' in instructions_modified[instruction_to_change]:
        instructions_modified[instruction_to_change] = instructions_modified[instruction_to_change].replace('jmp',
                                                                                                            'nop')
    else:
        instructions_modified[instruction_to_change] = instructions_modified[instruction_to_change].replace('nop',
                                                                                                            'jmp')

    runt_instructions = []
    acc = 0
    current_instruction = 0

    program_terminates = False
    while 1:
        if current_instruction == len(instructions_modified):
            program_terminates = True
            break

        elif current_instruction not in runt_instructions:
            runt_instructions.append(current_instruction)

            instruction = instructions_modified[current_instruction]
            operation, argument = instruction.split(' ')
            argument = int(argument)

            if operation == 'acc':
                acc += argument
                current_instruction += 1
            elif operation == 'jmp':
                current_instruction += argument
            else:
                current_instruction += 1
        else:
            program_terminates = False
            break

    if program_terminates:
        break

print_part_2(acc)
