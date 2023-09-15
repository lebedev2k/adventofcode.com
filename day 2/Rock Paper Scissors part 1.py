#https://adventofcode.com/2022/day/2

# A, X - Rock
# B, Y - Paper
# C, Z - Scissors
round_score = {
    'A X': 1 + 3,
    'A Y': 2 + 6,
    'A Z': 3 + 0,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 1 + 6,
    'C Y': 2 + 0,
    'C Z': 3 + 3,
}
with open('input.txt') as f:
    rounds = f.read().split('\n')
    total_score = 0
    for round_position in rounds:
        total_score += round_score[round_position]
    print(total_score)
