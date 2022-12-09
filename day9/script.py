from os.path import abspath, dirname
import math

RIGHT = "R"
LEFT = "L"
UP = "U"
DOWN = "D"


def parse_input(input):
    result = []
    for line in input.split("\n"):
        command, value = line.split(" ")
        result += [(command, int(value))]
    return result


def calc_tail_position(tail_position, head_position):
    if tail_position[0] == head_position[0]:
        distance = tail_position[1] - head_position[1]
        if abs(distance) <= 1:
            return tail_position
        if distance > 0:
            return (tail_position[0], tail_position[1] - 1)
        return (tail_position[0], tail_position[1] + 1)
    if tail_position[1] == head_position[1]:
        distance = tail_position[0] - head_position[0]
        if abs(distance) <= 1:
            return tail_position
        if distance > 0:
            return (tail_position[0] - 1, tail_position[1])
        return (tail_position[0] + 1, tail_position[1])
    if (
        abs(tail_position[0] - head_position[0])
        + abs(tail_position[1] - head_position[1])
    ) <= 2:
        return tail_position
    if tail_position[0] < head_position[0] and tail_position[1] < head_position[1]:
        return (tail_position[0] + 1, tail_position[1] + 1)
    if tail_position[0] > head_position[0] and tail_position[1] > head_position[1]:
        return (tail_position[0] - 1, tail_position[1] - 1)
    if tail_position[0] < head_position[0] and tail_position[1] > head_position[1]:
        return (tail_position[0] + 1, tail_position[1] - 1)
    return (tail_position[0] - 1, tail_position[1] + 1)


def part_1(file):
    positions = {"0,0"}
    tail_position = (0, 0)
    head_position = (0, 0)
    for command, value in parse_input(file):
        if command == UP:
            for _ in range(value):
                head_position = (head_position[0], head_position[1] + 1)
                tail_position = calc_tail_position(tail_position, head_position)
                positions = {*positions, f"{tail_position[0]},{tail_position[1]}"}
        if command == DOWN:
            for _ in range(value):
                head_position = (head_position[0], head_position[1] - 1)
                tail_position = calc_tail_position(tail_position, head_position)
                positions = {*positions, f"{tail_position[0]},{tail_position[1]}"}
        if command == LEFT:
            for _ in range(value):
                head_position = (head_position[0] - 1, head_position[1])
                tail_position = calc_tail_position(tail_position, head_position)
                positions = {*positions, f"{tail_position[0]},{tail_position[1]}"}
        if command == RIGHT:
            for _ in range(value):
                head_position = (head_position[0] + 1, head_position[1])
                tail_position = calc_tail_position(tail_position, head_position)
                positions = {*positions, f"{tail_position[0]},{tail_position[1]}"}
    return len(positions)


def part_2(file):
    positions = {"0,0"}
    tails_size = 9
    tail_positions = [(0, 0) for _ in range(tails_size)]
    head_position = (0, 0)
    for command, value in parse_input(file):
        if command == UP:
            for _ in range(value):
                head_position = (head_position[0], head_position[1] + 1)
                for index, tail_position in enumerate(tail_positions):
                    tail_positions[index] = calc_tail_position(
                        tail_position,
                        head_position if index == 0 else tail_positions[index - 1],
                    )
                
                positions = {*positions, f"{tail_position[0]},{tail_position[1]}"}
        if command == DOWN:
            for _ in range(value):
                head_position = (head_position[0], head_position[1] - 1)
                for index, tail_position in enumerate(tail_positions):
                    tail_positions[index] = calc_tail_position(
                        tail_position,
                        head_position if index == 0 else tail_positions[index - 1],
                    )
                positions = {*positions, f"{tail_position[0]},{tail_position[1]}"}
        if command == LEFT:
            for _ in range(value):
                head_position = (head_position[0] - 1, head_position[1])
                for index, tail_position in enumerate(tail_positions):
                    tail_positions[index] = calc_tail_position(
                        tail_position,
                        head_position if index == 0 else tail_positions[index - 1],
                    )
                positions = {*positions, f"{tail_position[0]},{tail_position[1]}"}
        if command == RIGHT:
            for _ in range(value):
                head_position = (head_position[0] + 1, head_position[1])
                for index, tail_position in enumerate(tail_positions):
                    tail_positions[index] = calc_tail_position(
                        tail_position,
                        head_position if index == 0 else tail_positions[index - 1],
                    )
                positions = {*positions, f"{tail_position[0]},{tail_position[1]}"}
    return len(positions)


day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
print(part_2(file))
