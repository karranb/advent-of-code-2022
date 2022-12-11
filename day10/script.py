from os.path import abspath, dirname

NOOP = "noop"


def parse_input(input):
    result = []
    for line in input.split("\n"):
        splitted_line = line.split(" ")
        if len(splitted_line) == 1:
            result += [splitted_line]
        else:
            result += [(splitted_line[0], int(splitted_line[1]))]
    return result


def get_strength(cycles, cycle_n):
    return cycle_n * cycles[cycle_n - 1]


def part_1(file):
    cycles = []
    current_value = 1
    for command in parse_input(file):
        if command[0] == NOOP:
            cycles += [current_value]
        else:
            cycles += [current_value]
            cycles += [current_value]
            current_value += command[1]

    return (
        get_strength(cycles, 20)
        + get_strength(cycles, 60)
        + get_strength(cycles, 100)
        + get_strength(cycles, 140)
        + get_strength(cycles, 180)
        + get_strength(cycles, 220)
    )


def part_2(file):
    cycles = []
    crt_rows = [[]]
    current_value = 1

    def set_position_value(crt_rows, value):
        crt_row = crt_rows[-1] or []
        crt_position = len(crt_row) +1
        if (
            crt_position == value
            or crt_position == value + 1
            or crt_position == value + 2
        ):
            crt_row += ["#"]
        else:
            crt_row += ["."]
        crt_rows[-1] = crt_row
        if crt_position == 40:
            crt_rows += [[]]
        return crt_rows

    for command in parse_input(file):
        if command[0] == NOOP:
            cycles += [current_value]
            crt_rows = set_position_value(crt_rows, current_value)
        else:
            cycles += [current_value]
            crt_rows = set_position_value(crt_rows, current_value)
            cycles += [current_value]
            crt_rows = set_position_value(crt_rows, current_value)
            current_value += command[1]

    for row in crt_rows:
        print("".join(row))


day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
