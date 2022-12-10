import argparse
from dataclasses import dataclass, field
from typing import Union, List, Optional

TOTAL_SIZE = 70000000
UPDATE_SIZE = 30000000
@dataclass
class File:
    size: int
    name: str

@dataclass
class Directory:
    name: str
    parent: Optional['Directory']
    contents: List[Union[File, 'Directory']] = field(default_factory=list)

def find_subdir(parent: Directory, name):
    for child in parent.contents:
        match child:
            case Directory(name=x) if x == name: 
                return child
    raise Exception(f"Could not find {name} under {parent.name}")

def get_name(dirr: Directory):
    output = dirr.name
    curr = dirr.parent
    while curr != None:
        output = f"{curr.name}/{output}"
        curr = curr.parent

    return output

sizes = {}

def calc_size(dirr: Directory):
    output = 0
    for item in dirr.contents:
        match item:
            case File(size=s):
                output += s
            case Directory:
                output += calc_size(item)
    sizes[get_name(dirr)] = output
    return output

def parse_input(lines):
    root = Directory(name="/", parent=None)
    curr = root
    for line in lines:
        match line.strip().split():
            case ['$', 'cd', '..']:
                curr = curr.parent
            case ['$', 'cd', '/']:
                curr = root
            case ['$', 'cd', dir_name]:
                curr = find_subdir(curr, dir_name)
            case ['$', 'ls']: 
                pass
            case ['dir', dir_name]:
                curr.contents.append(Directory(name=dir_name, parent=curr))
            case [size, filename]:
                curr.contents.append(File(name=filename, size=int(size)))
    
    sizes[get_name(root)] = calc_size(root)
    return root

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        filetree = parse_input(f.readlines())
    
#    print(sum(filter(lambda x: x <= 100000, sorted(sizes.values()))))
    free_space = TOTAL_SIZE - sizes['/']
    needed = UPDATE_SIZE - free_space

    print(list(sorted(filter(lambda x: x[1] >= needed, sizes.items()), key=lambda x: x[1]))[0][1])

if __name__ == '__main__':
    main()
