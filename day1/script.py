from os.path import abspath, dirname


def get_elves_calories(file):
    elves = []
    current_elf = []
    for line in file.split("\n"):
        if not line:
            elves += [current_elf]
            current_elf = []
            continue
        current_elf += [int(line)]
    return [*elves, current_elf]


def part_1(file):
    elves = get_elves_calories(file)
    max_calories = -1
    for elf in elves:
        elf_calories = sum(elf)
        if elf_calories > max_calories:
            max_calories = elf_calories
    return max_calories


def part_2(file):
    elves = get_elves_calories(file)
    elves_summed_calories = map(lambda elf: sum(elf), elves)
    sorted_calories_desc = sorted(elves_summed_calories)[::-1]
    return sum(sorted_calories_desc[:3])


day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
print(part_2(file))
