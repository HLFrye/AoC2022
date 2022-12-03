import argparse

lookup = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def separate_groups(lines):
    for i in range(0, len(lines), 3):
        yield lines[i:i+3]

def find_badge_priority(group):
    for item in group[0]:
        if item in group[1] and item in group[2]:
            return(lookup.index(item))

def calculate(line):
    midpoint = int((len(line) - 1) / 2)
    part1 = line[:midpoint]
    part2 = line[midpoint:]
    for item in part1:
        if item in part2:
            return lookup.index(item)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        print(sum(map(find_badge_priority, separate_groups(f.readlines()))))

if __name__ == '__main__':
    main()