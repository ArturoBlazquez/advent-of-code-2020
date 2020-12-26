from utils import read_file, print_part_1, print_part_2

# -- PARSE INPUT -- #
cups = [int(letter) for letter in read_file('input.txt')[0]]


# -- PART 1 -- #
def move(cups_list):
    current_cup = cups_list[0]
    three_cups = cups_list[1:4]
    other_cups = cups_list[4:]

    cut_position = 0
    for i in range(1, 5):
        index_to_find = ((current_cup - 1 - i) % 9) + 1
        if index_to_find in other_cups:
            cut_position = other_cups.index(index_to_find) + 1
            break

    return other_cups[:cut_position] + three_cups + other_cups[cut_position:] + [current_cup]


for _ in range(100):
    cups = move(cups)

one_position = cups.index(1)
print_part_1(''.join([str(x) for x in cups[one_position + 1:] + cups[:one_position]]))


# -- PART 2 -- #
class Node:
    def __init__(self, data):
        self.label = data
        self.next_cup: Node = None
        self.previous_label_cup: Node = None


class LinkedList:
    def __init__(self):
        self.head: Node = None


def get_cups(cups_list):
    nodes = [Node(i) for i in range(1, 10)]
    cups_ret = LinkedList()
    first_cup_index = int(cups_list[0]) - 1
    cups_ret.head = nodes[first_cup_index]

    for i in [int(letter) for letter in cups_list[1:]]:
        cups_ret.head.next_cup = nodes[i - 1]
        cups_ret.head = nodes[i - 1]

    cups_ret.head.next_cup = nodes[first_cup_index]
    cups_ret.head = nodes[first_cup_index]

    for i in range(9):
        nodes[i].previous_label_cup = nodes[i - 1]

    for _ in range(8):
        cups_ret.head = cups_ret.head.next_cup

    cups_ret.head.next_cup = Node(10)
    cups_ret.head = cups_ret.head.next_cup
    cups_ret.head.previous_label_cup = nodes[9 - 1]

    for label in range(11, 1000001):
        cups_ret.head.next_cup = Node(label)
        cups_ret.head.next_cup.previous_label_cup = cups_ret.head
        cups_ret.head = cups_ret.head.next_cup

    cups_ret.head.next_cup = nodes[first_cup_index]
    nodes[0].previous_label_cup = cups_ret.head
    cups_ret.head = cups_ret.head.next_cup

    return cups_ret


def move_v2(cups_list: LinkedList):
    current_cup = cups_list.head
    three_cups = [current_cup.next_cup, current_cup.next_cup.next_cup, current_cup.next_cup.next_cup.next_cup]

    next_head = three_cups[2].next_cup

    cups_list.head = next_head
    current_cup.next_cup = next_head

    previous_label_cup = current_cup.previous_label_cup
    while previous_label_cup in three_cups:
        previous_label_cup = previous_label_cup.previous_label_cup

    cut_next = previous_label_cup.next_cup
    previous_label_cup.next_cup = three_cups[0]
    three_cups[2].next_cup = cut_next


cups = get_cups(read_file('input.txt')[0])

for _ in range(10000000):
    move_v2(cups)

while cups.head.label != 1:
    cups.head = cups.head.next_cup

print_part_2(cups.head.next_cup.label * cups.head.next_cup.next_cup.label)
