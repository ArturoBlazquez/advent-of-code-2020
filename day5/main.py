from utils import read_file, print_part_1, print_part_2

boarding_passes = read_file('input.txt')

# -- PART 1 -- #
highest_seat_id = 0
for boarding_pass in boarding_passes:
    row_in_binary = boarding_pass[:7].replace('B', '1').replace('F', '0')
    row = int(row_in_binary, 2)

    column_in_binary = boarding_pass[7:].replace('R', '1').replace('L', '0')
    column = int(column_in_binary, 2)

    seat_id = row * 8 + column

    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

print_part_1(highest_seat_id)

# -- PART 2 -- #
plane_rows = {}
for boarding_pass in boarding_passes:
    row_in_binary = boarding_pass[:7].replace('B', '1').replace('F', '0')
    row = int(row_in_binary, 2)

    column_in_binary = boarding_pass[7:].replace('R', '1').replace('L', '0')
    column = int(column_in_binary, 2)

    if row in plane_rows:
        plane_rows[row] = plane_rows[row] + [column]
    else:
        plane_rows[row] = [column]

for key in plane_rows:
    if len(plane_rows[key]) == 7 or len(plane_rows[key]) == 9:
        missing_row = key

for i in range(0, 8):
    if i not in plane_rows[missing_row]:
        print_part_2(missing_row * 8 + i)
