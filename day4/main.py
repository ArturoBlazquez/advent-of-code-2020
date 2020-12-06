import re

from utils import read_file, print_part_1, print_part_2


def parse_passports():
    passports_lines = read_file('input.txt')
    passports_unparsed = ' '.join(passports_lines).split('  ')

    passports = []
    for passport in passports_unparsed:
        passport_dict = {}

        items = passport.split(' ')

        for item in items:
            key, value = item.split(':')

            passport_dict[key] = value

        passports.append(passport_dict)

    return passports


passports = parse_passports()

# -- PART 1 -- #
numValid = 0
for passport in passports:
    if all(elem in passport for elem in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
        numValid += 1

print_part_1(numValid)


# -- PART 2 -- #
def is_byr_valid(byr):
    if re.match(r"^[0-9]{4}$", byr):
        if int(byr) in range(1920, 2002 + 1):
            return True
    return False


def is_iyr_valid(iyr):
    if re.match(r"^[0-9]{4}$", iyr):
        if int(iyr) in range(2010, 2020 + 1):
            return True
    return False


def is_eyr_valid(eyr):
    if re.match(r"^[0-9]{4}$", eyr):
        if int(eyr) in range(2020, 2030 + 1):
            return True
    return False


def is_hgt_valid(hgt):
    if re.match(r"^[0-9]*cm$", hgt):
        if int(hgt[:-2]) in range(150, 193 + 1):
            return True
    if re.match(r"^[0-9]*in$", hgt):
        if int(hgt[:-2]) in range(59, 76 + 1):
            return True
    return False


def is_hcl_valid(hcl):
    if re.match(r"^#[0-9,a-f]{6}$", hcl):
        return True
    return False


def is_ecl_valid(ecl):
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False


def is_pid_valid(pid):
    if re.match(r"^[0-9]{9}$", pid):
        return True
    return False


numValid = 0
for passport in passports:
    if all(elem in passport for elem in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):

        if not is_byr_valid(passport['byr']):
            continue

        if not is_iyr_valid(passport['iyr']):
            continue

        if not is_eyr_valid(passport['eyr']):
            continue

        if not is_hgt_valid(passport['hgt']):
            continue

        if not is_hcl_valid(passport['hcl']):
            continue

        if not is_ecl_valid(passport['ecl']):
            continue

        if not is_pid_valid(passport['pid']):
            continue

        numValid += 1

print_part_2(numValid)
