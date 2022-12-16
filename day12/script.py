from os.path import abspath, dirname
import sys
import math

sys.setrecursionlimit(1500)

INITIAL = "S"
INITIAL_ELEVATION = "a"
DESTINATION = "E"
DESTINATION_ELEVATION = "z"


def get_char_value(char):
    if char == DESTINATION:
        return ord(DESTINATION_ELEVATION) - 96
    if char == INITIAL:
        return ord(INITIAL_ELEVATION) - 96
    return ord(char) - 96


def parse_input(input):
    result = []

    for line in input.split("\n"):
        result += [[char for char in line]]
    return result

class Vertex:
    def __init__(self, i, j, char, matrix, distance=math.inf):
        self.i = i
        self.j = j
        self.char = char
        self.name = get_node_index(i, j)
        self.distance = distance
        offsets = ((-1, 0), (1, 0), (0, -1), (0, 1))
        self.neighbors = []
        self.was_visited = False
        for item in offsets:
            neighbor_i = i + item[0]
            neighbor_j = j + item[1]
            if (
                neighbor_i >= 0
                and neighbor_j >= 0
                and neighbor_i <= (len(matrix) - 1)
                and neighbor_j <= (len(matrix[neighbor_i]) - 1)
                and (get_char_value(matrix[i][j]))
                <= get_char_value(matrix[neighbor_i][neighbor_j]) + 1
            ):
                self.neighbors += [get_node_index(neighbor_i, neighbor_j)]

    def __str__(self):
        return f"{self.name} - {self.distance}"


def create_graph(matrix):
    vertexes = {}
    initial = None
    destination = None
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            v = Vertex(i, j, char, matrix)
            vertexes[v.name] = v
            initial = v if matrix[i][j] == INITIAL else initial
            destination = v if matrix[i][j] == DESTINATION else destination
    return vertexes, initial, destination


def get_node_index(i, j):
    return f"{i},{j}"


def get_min_non_visited_vertex(q):
    min_vertex = None
    for vertex in q:
        if (
            not min_vertex or vertex.distance < min_vertex.distance
        ) and not vertex.was_visited:
            min_vertex = vertex
    return min_vertex


def dijkstra(graph, destination):
    q = list(graph.values())
    destination.distance = 0
    while q:
        u = get_min_non_visited_vertex(q)
        q.remove(u)
        u.was_visited = True

        for neighbor in u.neighbors:
            neighbor_vertex = graph[neighbor]
            if not neighbor_vertex.was_visited:
                neighbor_vertex.distance = u.distance + 1
    return graph


def part_1(file):
    graph, initial, destination = create_graph(parse_input(file))
    dijkstra(graph, destination)
    return initial


def part_2(file):
    graph, _, destination = create_graph(parse_input(file))
    dijkstra(graph, destination)
    
    valid_vertexes_distances = []
    for vertex in graph.values():
        if vertex.char in ['a', INITIAL]:
            valid_vertexes_distances += [vertex.distance]
    return sorted(valid_vertexes_distances)[0]

day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
print(part_2(file))
