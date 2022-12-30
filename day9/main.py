import argparse

"""
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

class HeadSegment:
    def __init__(self, num_tails):
        self.head = [0, 0]
        self.tail = list(map(lambda _: [0, 0], range(num_tails)))
        self.tail_positions = set()
    
    def update_tail(self, tail_pos = 0):
        head = self.head if tail_pos == 0 else self.tail[tail_pos - 1]
        tail = self.tail[tail_pos]
        x_dist = abs(head[0] - tail[0])
        y_dist = abs(head[1] - tail[1])

        if x_dist > 1 and y_dist > 1:
            tail[0] = int(head[0] - ((head[0] - tail[0]) / x_dist))
            tail[1] = int(head[1] - ((head[1] - tail[1]) / y_dist))
        elif x_dist > 1:
            tail[0] = int(head[0] - ((head[0] - tail[0]) / x_dist))
            tail[1] = head[1]
        elif y_dist > 1:
            tail[0] = head[0]
            tail[1] = int(head[1] - ((head[1] - tail[1]) / y_dist))

        if tail_pos + 1 < len(self.tail):
            self.update_tail(tail_pos + 1)
        else:
            self.tail_positions.add(tuple(self.tail[tail_pos]))

    def move(self, instr):
        move, distance = instr
        distance = int(distance)
        for i in range(distance):
            match move:
                case 'R':
                    self.head[0] += 1
                case 'L':
                    self.head[0] -= 1
                case 'U': 
                    self.head[1] += 1
                case 'D':
                    self.head[1] -= 1
            self.update_tail()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    board = HeadSegment(9)
    with open(args.filename) as f:
        for line in f.readlines():
            board.move(line.strip().split())
    
    print(len(board.tail_positions))

if __name__ == '__main__':
    main()