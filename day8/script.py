from os.path import abspath, dirname


def parse_input_into_list(input):
    trees = []
    for line in input.split("\n"):
        trees += [[int(char) for char in line]]
    return trees


def get_is_tree_visible(trees, i, j):
    if i == 0 or i == (len(trees) - 1) or j == 0 or j == (len(trees[0]) - 1):
        return True
    is_visible = True
    for comparison_i in range(i):
        if trees[comparison_i][j] >= trees[i][j]:
            is_visible = False
            continue

    if is_visible:
        return True

    is_visible = True
    for comparison_i in range(i + 1, len(trees)):
        if trees[comparison_i][j] >= trees[i][j]:
            is_visible = False
            continue

    if is_visible:
        return True
    is_visible = True
    for comparison_j in range(j):
        if trees[i][comparison_j] >= trees[i][j]:
            is_visible = False
            continue

    if is_visible:
        return True

    is_visible = True
    for comparison_j in range(j + 1, len(trees[0])):
        if trees[i][comparison_j] >= trees[i][j]:
            return False
    return True


def part_1(file):
    trees = parse_input_into_list(file)
    visible_trees = []
    for i, row in enumerate(trees):
        for j, _ in enumerate(row):
            if get_is_tree_visible(trees, i, j):
                visible_trees += [(i, j)]
    return len(visible_trees)


def get_scenic_score(trees, i, j):
    if i == 0 or i == (len(trees) - 1) or j == 0 or j == (len(trees[0]) - 1):
        return 0
    viewing_distances = []

    for x, comparison_i in enumerate(range(i)[::-1]):
        if trees[comparison_i][j] >= trees[i][j]:
            viewing_distances += [x + 1]
            break
    if len(viewing_distances) != 1:
        viewing_distances += [i]

    for x, comparison_i in enumerate(range(i + 1, len(trees))):
        if trees[comparison_i][j] >= trees[i][j]:
            viewing_distances += [x + 1]
            break

    if len(viewing_distances) != 2:
        viewing_distances += [len(range(i + 1, len(trees)))]

    for x, comparison_j in enumerate(range(j)[::-1]):
        if trees[i][comparison_j] >= trees[i][j]:
            viewing_distances += [x + 1]
            break

    if len(viewing_distances) != 3:
        viewing_distances += [j]

    for x, comparison_j in enumerate(range(j + 1, len(trees[0]))):
        if trees[i][comparison_j] >= trees[i][j]:
            viewing_distances += [x + 1]
            break
    if len(viewing_distances) != 4:
        viewing_distances += [len(range(j + 1, len(trees[0])))]
    return (
        viewing_distances[0]
        * viewing_distances[1]
        * viewing_distances[2]
        * viewing_distances[3]
    )


def part_2(file):
    trees = parse_input_into_list(file)
    max_scenic_score = 0
    for i, row in enumerate(trees):
        for j, _ in enumerate(row):
            scenic_score = get_scenic_score(trees, i, j)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    return max_scenic_score


day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
print(part_2(file))
