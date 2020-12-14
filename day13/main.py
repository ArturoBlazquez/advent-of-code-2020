from utils import read_file, print_part_1, print_part_2, chinese_remainder_theorem

input = read_file('input.txt')

# -- PART 1 -- #
earliest_timestamp = int(input[0])
bus_ids = [int(bus_id) for bus_id in input[1].split(',') if bus_id != 'x']

depart_timestamp = earliest_timestamp
earliest_bus_id = 0
for i in range(10):
    for bus_id in bus_ids:
        if depart_timestamp % bus_id == 0:
            earliest_bus_id = bus_id
            break

    if earliest_bus_id != 0:
        break

    depart_timestamp += 1

print_part_1((depart_timestamp - earliest_timestamp) * earliest_bus_id)

# -- PART 2 -- #
moduli = []
remainders = []

buses = input[1].split(',')
for i in range(len(buses)):
    if buses[i] != 'x':
        moduli.append(int(buses[i]))
        remainders.append(-i)

print_part_2(chinese_remainder_theorem(moduli, remainders))
