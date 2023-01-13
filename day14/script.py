from os.path import abspath, dirname

def parse_input(input):
    result = []
    for line in input.split("\n"):
        if line != "":
            points = line.split(" -> ")
            result += [[map(int, point.split(",")) for point in points]]
    return result


def parse_wall_to_rocks(wall):
    current_x, current_y = wall[0]
    rocks = [[current_x, current_y]]

    for destination_x, destination_y in wall[1:]:
        while current_x != destination_x or current_y != destination_y:
            if current_x > destination_x:
                current_x -= 1
            elif current_x < destination_x:
                current_x += 1
            elif current_y > destination_y:
                current_y -= 1
            elif current_y < destination_y:
                current_y += 1
            rocks += [[current_x, current_y]]

    return rocks


def part_1(file):
    rocks = []
    for wall in parse_input(file):
        rocks += parse_wall_to_rocks(wall)
    index = {}
    for rock in rocks:
        index[f"{rock[0]},{rock[1]}"] = True

    def drop_sand(initial_x, initial_y):
        x = initial_x
        y = initial_y
        while True:
            if f"{x},{y}" in index:
                if f"{x-1},{y}" not in index:
                    x -= 1
                    continue
                elif f"{x+1},{y}" not in index:
                    x += 1
                    continue
                else:
                    index[f"{x},{y-1}"] = True
                    return False
            y += 1

            if y > 170:
                return True

    i = 0
    while True:
        has_ended = drop_sand(500, 0)
        if has_ended:
            break
        i += 1
    return i


def part_2(file):
    rocks = []
    for wall in parse_input(file):
        rocks += parse_wall_to_rocks(wall)
    index = {}
    max_y = -1
    for rock in rocks:
        index[f"{rock[0]},{rock[1]}"] = True
        if max_y < rock[1]:
            max_y = rock[1]
    max_y += 2
    floor = parse_wall_to_rocks(
        [
            [0, max_y],
            [1000, max_y],
        ]
    )
    for rock in floor:
        index[f"{rock[0]},{rock[1]}"] = True

    def drop_sand(initial_x, initial_y):
        x = initial_x
        y = initial_y
        while True:
            if f"{x},{y}" in index:
                if f"{x-1},{y}" not in index:
                    x -= 1
                    continue
                elif f"{x+1},{y}" not in index:
                    x += 1
                    continue
                else:
                    if y - 1 == 0:
                        return True
                    index[f"{x},{y-1}"] = True
                    return False
            y += 1

    i = 0
    while True:
        i += 1
        has_ended = drop_sand(500, 0)
        if has_ended:
            break
    return i


day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
print(part_2(file))
