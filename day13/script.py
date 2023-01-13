from os.path import abspath, dirname
import math


class Node:
    def __init__(self, parent=None):
        self.parent = parent
        self.values = []

    def add_value(self, value):
        self.values += [value]



def parse_line(line):
    head = Node()
    current = head
    value = ""
    for char in line:
        if char == "[":
            new = Node(current)
            current.add_value(new)
            current = new
        elif char == "]":
            if value:
                current.add_value(int(value))
            value = ""
            current = current.parent
        elif char == ",":
            if value:
                current.add_value(int(value))
            value = ""
        else:
            value += char
    return head


def parse_input(input):
    result = []
    current = []
    for line in input.split("\n"):
        if line != "":
            head = parse_line(line)
            current += [head]
            if len(current) == 2:
                result += [current]
                current = []
    return result


def check_packet_pair(packet_1, packet_2):
    if len(packet_1.values) == 0 and len(packet_2.values) == 0:
        return True
    print(packet_1.values, packet_2.values)
    for index, packet_1_value in enumerate(packet_1.values):
        print('hum', index)
        if type(packet_1_value) == int:
            if index <= len(packet_2.values) - 1:
                packet_2_value = packet_2.values[index]
                if type(packet_2_value) == int:
                    if packet_1_value < packet_2_value:
                        return True
                    if packet_2_value < packet_1_value:
                        return False
                else:
                    transformed_packet = Node()
                    transformed_packet.add_value(packet_1_value)
                    result = check_packet_pair(transformed_packet, packet_2_value)
                    if result == True or result == False:
                        return result
            else:
                return False
        else:
            if index <= len(packet_2.values) - 1:
                packet_2_value = packet_2.values[index]
                if type(packet_2_value) == int:
                    transformed_packet = Node()
                    transformed_packet.add_value(packet_2)
                    result = check_packet_pair(packet_1_value, transformed_packet)
                    if result == True or result == False:
                        return result
                else:
                    print('aqui', packet_1_value, packet_2_value)
                    result = check_packet_pair(packet_1_value, packet_2_value)
                    if result == True or result == False:
                        return result
            else:
                return False
    if len(packet_1.values) < len(packet_2.values):
        return True
    if len(packet_1.values) > len(packet_2.values):
        return False
    return None


def part_1(file):
    packets_pairs = parse_input(file)
    result = 0
    for index, packet_pair in enumerate(packets_pairs):
        if check_packet_pair(*packet_pair):
            print(index + 1)
            result += index + 1

    return result


def part_2(file):
    return 0


day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
print(part_2(file))
