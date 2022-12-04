import argparse

"""
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

def has_full_overlap(line):
    first, second = line.split(",")
    a1, a2 = list(map(int, first.split("-")))
    b1, b2 = list(map(int, second.split("-")))
    if b1 in range(a1, a2+1): return True
    if b2 in range(a1, a2+1): return True
    if a1 in range(b1, b2+1): return True
    if a2 in range(b1, b2+1): return True
    return False



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        print(len(list(filter(has_full_overlap, f.readlines()))))

if __name__ == '__main__':
    main()