from utils import read_file, print_part_1, print_part_2

num_list = [int(line) for line in read_file('input.txt')]


# -- PART 1 -- #
def any_sum_to(list_to_sum, sum):
    for i in range(len(list_to_sum)):
        for j in range(i, len(list_to_sum)):
            if list_to_sum[i] + list_to_sum[j] == sum:
                return True

    return False


for i in range(25, len(num_list) + 1):
    if not any_sum_to(num_list[i - 25:i], num_list[i]):
        break

print_part_1(num_list[i])

# -- PART 2 -- #
i = 0
j = 1
while 1:
    contiguous_sum = sum(num_list[i:j])
    if contiguous_sum < 88311122:
        j += 1
    elif contiguous_sum > 88311122:
        i += 1
    else:
        break

print_part_2(min(num_list[i:j]) + max(num_list[i:j]))
