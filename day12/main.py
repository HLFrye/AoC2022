import argparse
from dataclasses import dataclass
import bisect
import math
from typing import List, Tuple
from functools import partial
from collections import defaultdict
import sys

# Keep a list of possible places to explore from
# List should include coord, shortest path to coord, 

class SearchQueue:
    def __init__(self, board):
        self._queue = []
        self._best = defaultdict(lambda: sys.maxsize)
        self.board = board

    def score_point(self, pt):
        """
        Score calculation will be:
        Distance From Goal - Length of Path
        """
        a = pt.pos[0] - self.board.end[0]
        b = pt.pos[1] - self.board.end[1]
        c = pt.pos[2] - self.board.end[2]
        # return math.sqrt(a**2 + b**2 + c**2) - len(pt.path)
        return len(pt.path)

    def add(self, item):
        bisect.insort(self._queue, item, key=self.score_point)

    def pop(self):
        while True:
            next = self._queue.pop(0)
            if len(next.path) < self._best[next.pos]:
                self._best[next.pos] = len(next.path)
                return next

MapPoint = Tuple[int, int, int]

@dataclass
class SearchPoint:
    pos: MapPoint
    path: List[MapPoint]

@dataclass
class Board:
    map: List[List[str]]
    start: MapPoint
    low_points: List[MapPoint]
    end: MapPoint

def add(pt: MapPoint, y: Tuple[int, int]):
    return (pt[0] + y[0], pt[1] + y[1])

def get_height(board, pos):
    height = board.map[pos[1]][pos[0]]
    match height:
        case 'S':
          return ord('a')
        case 'E':
          return ord('z')
        case x:
          return ord(x)

def in_range(board, pt):
    return (
        pt[0] >= 0 and
        pt[0] < len(board.map[0]) and
        pt[1] >= 0 and
        pt[1] < len(board.map)
    )

def travel(board):
    visited = set()

    def get_options(pt):
        output = []
        cardinals = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        next_pts = map(partial(add, pt.pos), cardinals)
        valid_pts = filter(partial(in_range, board), next_pts)
        pts_with_height = map(lambda x: (x[0], x[1], get_height(board, x)), valid_pts)
        available_pots = filter(lambda x: x[2] <= pt.pos[2] + 1, pts_with_height)
        final_searchpoints = map(lambda x: SearchPoint(pos=x, path=[*pt.path, x]), available_pots)
        return final_searchpoints

    heads = SearchQueue(board)
    heads.add(SearchPoint(pos=board.start, path=[]))
    for pt in board.low_points:
        heads.add(SearchPoint(pos=pt, path=[]))

    final = None
    while True:
        curr = heads.pop()
        if curr.pos == board.end:
            final = curr
            break
        for next in get_options(curr):
            heads.add(next)

    # print(repr(final))
    if len(final.path) in (726,):
        print(f"Still wrong answer {len(final.path) = }")
    print(len(final.path))
    for y, line in enumerate(board.map):
        output = ""
        for x, height in enumerate(line):
            if (x, y, ord(height)) in final.path:
                chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                output += chars[(final.path.index((x, y, ord(height))) % len(chars))]
            else:
                output += "."
        print(output)

            
def read_board(lines):
    pts = list(map(lambda x: x.strip(), lines))
    start = None
    end = None
    start_pts = []
    for y, line in enumerate(pts):
        a_xs = filter(lambda x: x[1] == 'a', enumerate(line))
        a_pts = map(lambda x: (x[0], y, ord('a')), a_xs)
        start_pts += list(a_pts)
        if "S" in line:
            x = line.index("S")
            start = (x, y, ord('a'))
        if "E" in line:
            x = line.index("E")
            end = (x, y, ord('z'))
    return Board(map=pts, start=start, end=end, low_points=start_pts)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        board = read_board(f.readlines())

    travel(board)
    


if __name__ == '__main__':
    main()