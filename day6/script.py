from os.path import abspath, dirname


def find_first_packet(packet, packet_size=4):
    for iteration_index, _ in enumerate(packet[packet_size - 1 :]):
        index = iteration_index + packet_size
        if len(set(packet[index - packet_size : index])) == packet_size:
            return index
    return -1


def part_1(file):
    return find_first_packet(file)


def part_2(file):
    return find_first_packet(file, 14)


day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
print(part_2(file))
