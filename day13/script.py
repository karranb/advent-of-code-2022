from os.path import abspath, dirname
import functools


def parse_array(line_slice):
    array = []
    current_value = ""
    left = 0
    while left < len(line_slice):
        char = line_slice[left]
        if char == ",":
            if current_value:
                array += [int(current_value)]
            current_value = ""
        elif char == "[":
            parsed_array, result_left = parse_array(line_slice[left + 1 :])
            array += [parsed_array]
            left += result_left + 2
        elif char == "]":
            if current_value:
                array += [int(current_value)]
            return array, left
        else:
            current_value += char

        left += 1
    return array, left


def parse_input(input):
    result = []
    current = []
    for line in input.split("\n"):
        if line != "":
            array = parse_array(line[1:])[0]
            current += [array]
            if len(current) == 2:
                result += [current]
                current = []
    return result


def check_packet_pair(packet_1, packet_2):
    left = 0
    while left < len(packet_1):
        packet_1_item = packet_1[left]
        if left == len(packet_2):
            return False
        packet_2_item = packet_2[left]
        if type(packet_1_item) == int and type(packet_2_item) == int:
            if packet_1_item < packet_2_item:
                return True
            if packet_1_item > packet_2_item:
                return False
        if type(packet_1_item) == int and type(packet_2_item) == list:
            result = check_packet_pair([packet_1_item], packet_2_item)
            if result is not None:
                return result
        if type(packet_1_item) == list and type(packet_2_item) == int:
            result = check_packet_pair(packet_1_item, [packet_2_item])
            if result is not None:
                return result
        if type(packet_1_item) == list and type(packet_2_item) == list:
            result = check_packet_pair(packet_1_item, packet_2_item)
            if result is not None:
                return result
        left += 1
    if len(packet_1) > len(packet_2):
        return False
    if len(packet_1) < len(packet_2):

        return True
    return None


def compare_packet_pair(packet_1, packet_2):
    check = check_packet_pair(packet_1, packet_2)
    return 0 if check is None else 1 if check is False else -1


def part_1(file):
    packet_pairs = parse_input(file)
    result = 0
    for index, packet_pair in enumerate(packet_pairs):
        if check_packet_pair(*packet_pair) is not False:
            result += index + 1

    return result


def part_2(file):
    packets = []
    new_input = parse_input(
        """
[[2]]
[[6]]
    """
    )
    old_input = parse_input(file)
    for packet_1, packet_2 in old_input + new_input:
        packets += [packet_1, packet_2]
    packets = sorted(packets, key=functools.cmp_to_key(compare_packet_pair))
    return (packets.index(new_input[0][0]) + 1) * (packets.index(new_input[0][1]) + 1)


day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
print(part_2(file))
