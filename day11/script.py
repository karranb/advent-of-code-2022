from os.path import abspath, dirname

SUM = "+"
SUBRATCT = "-"
DIVIDE = "/"
MULTIPLY = "*"
OLD = "old"


class Monkey:
    def __init__(
        self, operation, starting_items, test, test_true_index, test_false_index
    ):
        self.inspections = 0
        self.items = [int(item) for item in starting_items]
        self.test = int(test)
        self.test_true_index = int(test_true_index)
        self.test_false_index = int(test_false_index)
        self.operation = operation

    def get_operation_result(self, item):
        number_1, operation_action, number_2 = self.operation.split(" ")
        number_1 = item if number_1 == OLD else int(number_1)
        number_2 = item if number_2 == OLD else int(number_2)
        if operation_action == SUM:
            return number_1 + number_2
        if operation_action == SUBRATCT:
            return number_1 - number_2
        if operation_action == MULTIPLY:
            return number_1 * number_2
        if operation_action == DIVIDE:
            return number_1 / number_2

    def inspect(self, monkeys_multiplied_divisors=None):
        if not len(self.items):
            return
        item = self.items[0]
        if not monkeys_multiplied_divisors:
            item_inspection_result = int(self.get_operation_result(item) / 3)
        else:
            item_inspection_result = int(self.get_operation_result(item) % monkeys_multiplied_divisors)
            
        self.inspections += 1
        self.items = self.items[1:]
        return (
            item_inspection_result,
            self.test_true_index
            if item_inspection_result % self.test == 0
            else self.test_false_index,
        )

    def add_item(self, item):
        self.items = [*self.items, item]


def parse_input(input):
    result = []
    starting_items = None
    operation = None
    test = None
    test_true_index = None
    test_false_index = None

    for line in input.split("\n"):
        if "Starting items" in line:
            _, raw_starting_items = line.split(": ")
            starting_items = raw_starting_items.split(", ")
            continue
        if "Operation" in line:
            _, raw_operation = line.split(": ")
            operation = raw_operation.split(" = ")[1]
            continue
        if "Test: divisible by " in line:
            test = line.split("Test: divisible by ")[1]
            continue
        if "If true: throw to monkey " in line:
            test_true_index = line.split("If true: throw to monkey ")[1]
            continue
        if "If false: throw to monkey " in line:
            test_false_index = line.split("If false: throw to monkey ")[1]
            result += [
                Monkey(
                    operation, starting_items, test, test_true_index, test_false_index
                )
            ]
            starting_items = None
            operation = None
            test = None
            test_true_index = None
            test_false_index = None
            continue
    return result


def part_1(file):
    monkeys = parse_input(file)
    round = 0
    while round < 20:
        for monkey in monkeys:
            for _ in monkey.items:
                item, new_index = monkey.inspect()
                monkeys[new_index].add_item(item)
        round += 1

    biggest_inspections = sorted([monkey.inspections for monkey in monkeys])[-2:]
    return biggest_inspections[0] * biggest_inspections[1]


def part_2(file):
    monkeys = parse_input(file)
    round = 0
    multiplied_tests = 1
    for monkey in monkeys:
        multiplied_tests *= monkey.test
    while round < 10000:
        for monkey in monkeys:
            for _ in monkey.items:
                item, new_index = monkey.inspect(multiplied_tests)
                monkeys[new_index].add_item(item)
        round += 1

    biggest_inspections = sorted([monkey.inspections for monkey in monkeys])[-2:]
    return biggest_inspections[0] * biggest_inspections[1]

day_path = dirname(abspath(__file__))
file = open(f"{day_path}/input.txt", "r").read()

print(part_1(file))
print(part_2(file))
