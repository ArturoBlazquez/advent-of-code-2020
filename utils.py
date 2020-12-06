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
