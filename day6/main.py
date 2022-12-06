import argparse

PACKET_LENGTH = 14

def find_start(line):
    buf = ""
    def done():
        return len(buf) == PACKET_LENGTH and len(set(buf)) == PACKET_LENGTH
        
    for index, char in enumerate(line):
        buf += char
        buf = buf[-PACKET_LENGTH:]
        if done():
            return index+1

def process(lines):
    for line in lines:
        print(find_start(line))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        process(f.readlines())

if __name__ == '__main__':
    main()