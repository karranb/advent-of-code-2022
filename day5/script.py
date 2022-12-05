from os.path import abspath, dirname
import math

def parse_stacks_and_commands(file):
    stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    commands = []
    stacks_ended = False
    for line in file.split("\n"):
        if not stacks_ended and '[' not in line:
            stacks_ended = True
            continue
        if not stacks_ended:
            for index, char  in enumerate(line):
                if char == '[':
                    stack_index = math.ceil(index / 4) + 1
                    stacks[stack_index] = [line[index+1]] + stacks[stack_index]
        if "move" in line:
            commands += [line.replace("move", "").replace("from", "").replace("to", "").replace("  ", " ").strip()]
    return stacks, commands


def part_1(file):
    stacks, commands = parse_stacks_and_commands(file)
    for command in commands:
        move_n, stack_from, stack_to = command.split(' ')
        item = 0
        while item < int(move_n):
            stacks[int(stack_to)] += [stacks[int(stack_from)][-1]]
            stacks[int(stack_from)] = stacks[int(stack_from)][:-1]
            item += 1
    result = ''
    for item in stacks.values():
        result += item[-1]
    return result


def part_2(file):
    stacks, commands = parse_stacks_and_commands(file)
    for command in commands:
        move_n, stack_from, stack_to = command.split(' ')
        stacks[int(stack_to)] += stacks[int(stack_from)][-int(move_n):]
        stacks[int(stack_from)] = stacks[int(stack_from)][:-int(move_n)]
    result = ''
    for item in stacks.values():
        result += item[-1]
    return result

day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
print(part_2(file))
