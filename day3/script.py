from os.path import abspath, dirname


def parse_rubsacks(file):
    rucksacks = []
    for line in file.split("\n"):
        compartiment_size = int(len(line) / 2)
        rucksacks += [[line[:compartiment_size], line[compartiment_size:]]]
    return rucksacks


def get_letter_value(letter):
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    lowered_letter = letter.lower()
    lower_value = letters.index(lowered_letter) + 1
    if letter == lowered_letter:
        return lower_value
    return lower_value + len(letters)


def part_1(file):
    rucksacks = parse_rubsacks(file)
    matches = []

    def get_match(
        compartiment1,
        compartiment2,
    ):
        for item in compartiment1:
            if item in compartiment2:
                return item

    for rucksack in rucksacks:
        matches += [get_match(rucksack[0], rucksack[1])]
    total = 0
    for item in matches:
        total += get_letter_value(item)
    return total


def part_2(file):
    rucksacks = parse_rubsacks(file)
    left = 0
    elves_group_size = 3
    matches = []

    def get_match(rucksack_1, rucksack_2, rucksack_3):
        for item in rucksack_1:
            if item in rucksack_2 and item in rucksack_3:
                return item

    while left < len(rucksacks):
        rucksack_1 = rucksacks[left][0] + rucksacks[left][1]
        rucksack_2 = rucksacks[left + 1][0] + rucksacks[left + 1][1]
        rucksack_3 = rucksacks[left + 2][0] + rucksacks[left + 2][1]
        matches += [get_match(rucksack_1, rucksack_2, rucksack_3)]
        left += elves_group_size
    total = 0
    for item in matches:
        total += get_letter_value(item)
    return total


day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
print(part_2(file))
