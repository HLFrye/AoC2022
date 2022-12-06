import argparse
from enum import Enum
from collections import defaultdict
import re

class InputMode(Enum):
    READ_ITEMS = 0,
    READ_INSTRUCTIONS = 1

def process_instruction_9000(stacks, move, frm, to):
    move = int(move)
    for i in range(move):
        x = stacks[frm].pop(0)
        stacks[to].insert(0, x)

def process_instruction_9001(stacks, move, frm, to):
    move = int(move)
    x = stacks[frm][0:move]
    stacks[frm] = stacks[frm][move:]
    stacks[to] = x + stacks[to]


def parse_input(lines):
    mode = InputMode.READ_ITEMS
    stacks = defaultdict(list)
    for line in lines:
        if len(line.strip()) == 0:
            mode = InputMode.READ_INSTRUCTIONS
            continue

        if mode == InputMode.READ_ITEMS:
            for i in range(1, len(line), 4):
                stack_name = str(int(1 + ((i - 1) / 4)))
                val = line[i:i+1].strip()
                if str(val) != stack_name and len(val) != 0:
                    stacks[stack_name].append(val)

        if mode == InputMode.READ_INSTRUCTIONS:
            match = re.match(r"move (?P<move>\d+) from (?P<frm>\d+) to (?P<to>\d+)", line)
            move = match.group("move")
            frm = match.group("frm")
            to = match.group("to")
            process_instruction_9001(stacks, move, frm, to)

    keys = sorted(stacks.keys())
    output = ""
    for key in keys:
        output += stacks[key][0]

    print(output)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        parse_input(f.readlines())

if __name__ == "__main__":
    main()