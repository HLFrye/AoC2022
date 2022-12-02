import argparse

result = [
    3, 0, 6
]

"""
The winner of the whole tournament is the player 
with the highest score. Your total score is the 
sum of your scores for each round. The score for
a single round is the score for the shape you 
selected (1 for Rock, 2 for Paper, and 3 for 
Scissors) plus the score for the outcome of 
the round (0 if you lost, 3 if the round was a 
draw, and 6 if you won).

"""

"""
"Anyway, the second column says how the round 
needs to end: X means you need to lose, Y means 
you need to end the round in a draw, and Z means 
you need to win. Good luck!"
"""

"""
A X - mine = 2
B X - mine = 0
"""

def score_game(line):
    theirs, goal = map(ord, line.split())
    theirs = theirs - ord('A')
    goal = goal - ord('X')
    mine = (theirs + (goal - 1)) % 3
    score = (mine + 1) + result[(3 + (theirs - mine))%3]
    return score
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    
    with open(args.filename) as f:
        print(sum(map(score_game, f.readlines())))

if __name__ == '__main__':
    main()
