import argparse
from dataclasses import dataclass
from functools import cmp_to_key


def parse_packet(input_list):
    return list(map(lambda x: eval(x.strip()), input_list))
 
def compare(x, y):
    match x, y:
        case int(x), int(y):
            diff = x - y
            return diff if diff == 0 else diff // abs(diff)
        case list(x), int(y):
            return compare(x, [y])
        case int(x), list(y):
            return compare([x], y)
        case list(x), list(y):
            for i in range(min(len(x), len(y))):
                res = compare(x[i], y[i])
                if res != 0:
                    return res
            else:
                return compare(len(x), len(y))

def is_misordered(packet):
    return compare(packet[0], packet[1]) == 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    packets = []
    curr_packet = []
    with open(args.filename) as f:
        for i, line in enumerate(f.readlines()):
            if i % 3 < 2:
                curr_packet.append(line.strip())
            else:
                packets.append(curr_packet)
                curr_packet = []
    packets.append(curr_packet)
    parsed_packets = map(parse_packet, packets)
    combined_packets = sum(parsed_packets, [[[2]], [[6]]])
    sorted_packets = sorted(combined_packets, key=cmp_to_key(compare))
    first_idx = sorted_packets.index([[2]]) + 1
    second_idx = sorted_packets.index([[6]]) + 1
    print(first_idx * second_idx)

    # numbered_packets = enumerate(parsed_packets, start=1)
    # ordered_packets = filter(lambda x: not is_misordered(x[1]), numbered_packets)
    # ordered_indicies = map(lambda x: x[0], ordered_packets)
    # output = sum(ordered_indicies)
    # print(output)

if __name__ == '__main__':
    main()