from os.path import abspath, dirname


class Node:
    def __init__(self, name, parent=None, size=None):
        self.parent = parent
        self.size = size
        self.name = name
        self.children = {}

    def add_child(self, node):
        self.children[node.name] = node

    def __str__(self):
        return self.name


def parse_input_to_filesystem(input):
    commands = []
    listing_dir = False
    current_node = None

    for line in input.split("\n"):
        if line[0] == "$":
            listing_dir = False
            command = line[2:].strip()
            commands += [command]
            splitted_command = command.split(" ")
            if splitted_command[0] == "cd":
                if splitted_command[1] == "..":
                    current_node = current_node.parent
                elif splitted_command[1] == "/":
                    current_node = Node("/")
                else:
                    current_node = current_node.children[splitted_command[1]]
            if splitted_command[0] == "ls":
                listing_dir = True
        else:
            if listing_dir:
                splitted_line = line.split(" ")
                if splitted_line[0] == "dir":
                    current_node.add_child(Node(splitted_line[1], parent=current_node))
                else:
                    current_node.add_child(
                        Node(
                            splitted_line[1],
                            size=int(splitted_line[0]),
                            parent=current_node,
                        )
                    )
    while current_node.parent != None:
        current_node = current_node.parent
    return current_node


def get_size(node):
    if node.size:
        return node.size
    return sum(map(get_size, node.children.values()))


def get_all_at_most_100000_size_folders(node):
    folders = []
    for child in node.children.values():
        if child.size:
            continue
        folders += get_all_at_most_100000_size_folders(child)
    if get_size(node) <= 100000:
        folders = [node] + folders
    return folders


def part_1(file):
    root = parse_input_to_filesystem(file)
    at_most_100000 = get_all_at_most_100000_size_folders(root)
    return sum(map(get_size, at_most_100000))


def get_all_folders(node):
    folders = []
    if node.size:
        return folders
    for child in node.children.values():
        folders += get_all_folders(child)
    return [node] + folders
    # return [node] + list(map(get_all_folders, node.children.values()))


def part_2(file):
    root = parse_input_to_filesystem(file)
    root_size = get_size(root)
    filesystem_size = 70000000
    needed_unused_space = 30000000

    needed_space = needed_unused_space - (filesystem_size - root_size)

    best_folder = None
    best_diff = None

    for folder in get_all_folders(root):
        folder_size = get_size(folder)
        if folder_size < needed_space:
            continue
        if folder_size > needed_space:
            diff = folder_size - needed_space
            if not best_folder or diff < best_diff:
                best_folder = folder
                best_diff = diff
    return get_size(best_folder)


day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
print(part_2(file))
