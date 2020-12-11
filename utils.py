import functools
import os
import sys


def read_file(file_name):
    with open(os.path.join(sys.path[0], file_name)) as f:
        lines = f.readlines()
        return [line.rstrip("\n") for line in lines]


def print_part_1(text):
    print("Part 1: " + str(text))


def print_part_2(text):
    print("Part 2: " + str(text))


def contains_all(list1, list2):
    return all(elem in list1 for elem in list2)


def contains_any(list1, list2):
    return any(elem in list1 for elem in list2)


def duplicates(my_list):
    seen = set()
    uniq = []
    repeated = []
    for x in my_list:
        if x not in seen:
            uniq.append(x)
            seen.add(x)
        else:
            repeated.append(x)

    return set(repeated)


def lists_are_equal(list1, list2):
    if len(list1) != len(list2):
        return False

    return functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, list1, list2), True)


def matrix_are_equal(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        return False

    for i in range(len(matrix1)):
        if not lists_are_equal(matrix1[i], matrix2[i]):
            return False

    return True
