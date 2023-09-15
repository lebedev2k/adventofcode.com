#https://adventofcode.com/2022/day/2

# A, X - Rock
# B, Y - Paper
# C, Z - Scissors
round_score = [
    [3,4,8],
    [1,5,9],
    [2,6,7]
]
player1 = 'ABC'
player2 = 'XYZ'

with open('input.txt') as f:
    rounds = f.read().split('\n')
    total_score = 0
    for round_position in rounds:
        a, b = round_position.split()
        total_score += round_score[player1.find(a)][player2.find(b)]
    print(total_score)
