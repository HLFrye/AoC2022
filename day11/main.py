import argparse
from functools import reduce

class Monkey:
    def __init__(self, name, items, operation, test, true_case, false_case):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.true_case = true_case
        self.false_case = false_case
        self.items_handled = 0

    def add_item(self, item):
        self.items.append(item)

    def think(self, monkeys):
        """
        Monkey 0:
        Monkey inspects an item with a worry level of 79.
            Worry level is multiplied by 19 to 1501.
            Monkey gets bored with item. Worry level is divided by 3 to 500.
            Current worry level is not divisible by 23.
            Item with worry level 500 is thrown to monkey 3.
        """
#        print(f"Monkey {self.name}")
        while len(self.items) > 0:
            self.items_handled += 1
            old = self.items.pop(0)
#            print(f"  Monkey inspects an item with a worry level of {old}.")
            new = eval(self.operation)
#            print(f"  Worry level operation is {self.operation} with {old = } and {new = }")
            new = new % (reduce(lambda x, a: x * a, map(lambda x: x.test, monkeys)))
            # new = new // 3
#            print(f"  Monkey gets bored with item. Worry level is divided by 3 to {new}.")
            # print(f"{self.name = } { old = } { new = } { self.operation = }")
            if (new % self.test) == 0:
#                print(f"    Current worry level is divisible by {self.test}.")
                monkeys[self.true_case].add_item(new)
#                print(f"    Item with worry level {new} is thrown to monkey {self.true_case}")
            else:
#                print(f"    Current worry level is not divisible by {self.test}.")
                monkeys[self.false_case].add_item(new)
#                print(f"    Item with worry level {new} is thrown to monkey {self.false_case}")

def read_monkeys(lines):
    lines = list(lines)
    monkeys = []
    print(len(lines))
    for i in range((len(lines) // 7) + 1):
        monkey_start = i * 7
        monkey_end = (i+1) * 7
        monkey_info = lines[monkey_start:monkey_end]
        name = monkey_info[0].split(" ")[1][0:-1]
        items = list(map(int, monkey_info[1].strip().split(": ")[1].split(", ")))
        operation = monkey_info[2].strip().split("= ")[1]
        test = int(monkey_info[3].strip().split("divisible by ")[1])
        true_case = int(monkey_info[4].strip().split("throw to monkey ")[1])
        false_case = int(monkey_info[5].strip().split("throw to monkey ")[1])

 #       print(f"{items = } {operation = } {test = } { true_case = } { false_case = }")
        monkeys.append(Monkey(name, items, operation, test, true_case, false_case))
    
    return monkeys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        monkeys = read_monkeys(f.readlines())
    
    for i in range(10000):
        for monkey in monkeys:
            monkey.think(monkeys)
        top_two = list(sorted(monkeys, key=lambda x: x.items_handled, reverse=True))[0:2]
        print(f"{i = } | {top_two[0].items_handled * top_two[1].items_handled} ")


    print(list(map(lambda x: x.items_handled, monkeys)))
    
if __name__ == '__main__':
    main()