#https://adventofcode.com/2022/day/3

with open('day 3\input.txt') as f:
    a = f.readlines()
    total = 0
    for r in a:
        r = r.strip()
        part1 = r[0:len(r)//2]
        part2 = r[len(r)//2:len(r)]
        
print(ord('a')) #97-122
print(ord('z'))
print(ord('A')) #65-90
print(ord('Z'))