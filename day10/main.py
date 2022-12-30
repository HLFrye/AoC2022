import argparse

class Processor:
    def __init__(self):
        self.breakpoints = [20, 60, 100, 140, 180, 220]
        self.register = 1
        self.cycle = 0
        self.captures = {}

    def run(self, lines):
        for line in lines:
            match line.strip().split():
                case ["noop"]:
                    self.cycle += 1
                    self.check_breakpoints()
                    yield self.register
                case ["addx", val]:
                    self.cycle += 1
                    self.check_breakpoints()
                    yield self.register
                    self.cycle += 1
                    self.check_breakpoints()
                    yield self.register
                    self.register += int(val)

    def check_breakpoints(self):
        if self.cycle in self.breakpoints:
            self.captures[self.cycle] = self.register



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    proc = Processor()
    with open(args.filename) as f:
        line = ""
        for i, x in enumerate(proc.run(f.readlines())):
            if i % 40 == 0:
                print(line)
                line = ""
            if abs((i % 40) - x) < 2:
                line += "X"
            else:
                line += " "
        print(line)

    print(sum(map(lambda x: x[0] * x[1], proc.captures.items())))

if __name__ == '__main__':
    main()