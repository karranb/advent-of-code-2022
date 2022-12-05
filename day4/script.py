from os.path import abspath, dirname


def parse_elves_pairs_sections(file):
    elves_pairs_sections = []
    for line in file.split("\n"):
        elves_pairs_sections += [
            [elf_section.split("-") for elf_section in line.split(",")]
        ]
    return elves_pairs_sections


def full_overlap(elf_1, elf_2):
    elf_1_left, elf_1_right = elf_1
    elf_2_left, elf_2_right = elf_2
    return (
        int(elf_1_left) >= int(elf_2_left) and int(elf_1_right) <= int(elf_2_right)
    ) or (int(elf_1_left) <= int(elf_2_left) and int(elf_1_right) >= int(elf_2_right))


def overlap(elf_1, elf_2):
    elf_1_left = int(elf_1[0])
    elf_1_right = int(elf_1[1])
    elf_2_left = int(elf_2[0])
    elf_2_right = int(elf_2[1])
    while elf_1_left <= elf_1_right:
        elf_2_left = int(elf_2[0])
        while elf_2_left <= elf_2_right:
            if elf_1_left == elf_2_left:
                return True
            elf_2_left += 1
        elf_1_left += 1
    return False


def part_1(file):
    elves_pair_sections = parse_elves_pairs_sections(file)
    count = 0
    for elf_1, elf_2 in elves_pair_sections:
        if full_overlap(elf_1, elf_2):
            count += 1
    return count


def part_2(file):
    elves_pair_sections = parse_elves_pairs_sections(file)
    count = 0
    for elf_1, elf_2 in elves_pair_sections:
        if overlap(elf_1, elf_2):
            count += 1
    return count


day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
print(part_2(file))
