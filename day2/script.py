from os.path import abspath, dirname


def get_matches(file):
    matches = []
    for line in file.split("\n"):
        matches += [line.split(" ")]
    return matches


ROCK = "A"
PAPER = "B"
SCISSORS = "C"

secrets_index_part_1 = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}

victories_index = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}

points_index = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

VICTORY_POINTS = 6
DRAWING_POINTS = 3
LOOSING_POINTS = 0


def part_1(file):
    points = 0
    matches = get_matches(file)
    for enemy, you in matches:
        points += points_index[secrets_index_part_1[you]]
        if victories_index[secrets_index_part_1[you]] == enemy:
            points += VICTORY_POINTS
        elif enemy == secrets_index_part_1[you]:
            points += 3
    return points


secrets_index_part_2 = {"X": LOOSING_POINTS, "Y": DRAWING_POINTS, "Z": VICTORY_POINTS}


def part_2(file):
    points = 0
    matches = get_matches(file)
    for enemy, you in matches:
        points += secrets_index_part_2[you]
        if secrets_index_part_2[you] == DRAWING_POINTS:
            points += points_index[enemy]
        elif secrets_index_part_2[you] == LOOSING_POINTS:
            points += points_index[victories_index[enemy]]
        else:
            for winning_play, loosing_play in victories_index.items():
                if loosing_play == enemy:
                    points += points_index[winning_play]
                    continue
    return points


day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
print(part_2(file))
