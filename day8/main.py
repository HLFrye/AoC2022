import argparse
from functools import reduce, partial

def read_input(lines):
    output = []
    for line in lines:
        output.append(list(map(int, line.strip())))
    return output

def read_row(forest, row_num):
    return forest[row_num]

def read_col(forest, col_num):
    for row in forest:
        yield row[col_num]

def scan_line(line, dir):
    """
    Read a line either forward or backward, and yield every element that is
    visible on that line
    """
    start = 0 if dir == 1 else len(line) - 1
    end = len(line) - start - (0 if dir == 1 else 2)
    highest = -1
    for i in range(start, end, dir):
        height = line[i]
        if height > highest:
            highest = height
            yield i

def puzzle1(forest):
    visible_trees = set()
    for row in range(len(forest)):
        for col in scan_line(read_row(forest, row), 1):
            visible_trees.add((row, col))
        for col in scan_line(read_row(forest, row), -1):
            visible_trees.add((row, col))

    for col in range(len(forest[0])):
        for row in scan_line(list(read_col(forest, col)), 1):
            visible_trees.add((row, col))
        for row in scan_line(list(read_col(forest, col)), -1):
            visible_trees.add((row, col))

    return len(visible_trees)

def count_ray(forest, x, y, dir):
    steps = []
    match dir:
        case "north":
            steps = map(lambda y: (x, y), range(y-1, -1, -1))
        case "south":
            steps = map(lambda y: (x, y), range(y+1, len(forest)))
        case "east":
            steps = map(lambda x: (x, y), range(x+1, len(forest[y])))
        case "west":
            steps = map(lambda x: (x, y), range(x-1, -1, -1))

    output = 0
    height = forest[y][x]
    for x, y in steps:
        if height > forest[y][x]:
            output += 1
        else:
            output += 1
            break
    return output


def calc_scenic_level(forest, x, y):
    """
    Cast a ray from x, y in all four directions, count trees up to and including
    the first tree in the ray that is taller than this tree
    """
    directions = ["north", "south", "east", "west"]
    counter = partial(count_ray, forest, x, y)
    values = list(map(counter, directions))
    return reduce(lambda x, y: x * y, values, 1)

def puzzle2(forest):
    most_scenic = 0
    for y in range(len(forest)):
        for x in range(len(forest[0])):
            scenic_level = calc_scenic_level(forest, x, y)
            if scenic_level > most_scenic:
                most_scenic = scenic_level
    return most_scenic

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        forest = read_input(f.readlines())

    print(puzzle2(forest))

if __name__ == '__main__':
    main()