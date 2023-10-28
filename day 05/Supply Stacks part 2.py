# https://adventofcode.com/2022/day/5

from collections import deque

with open('input.txt') as f:
    stack_lines = []

    for line in f:
        if line.strip() == '':
            break
        else:
            stack_lines.append(line.rstrip('\n'))
    # generate stacks empty list
    stacks = []
    for _ in range(len(range(1, len(stack_lines[0]), 4))):
        stacks.append(deque())

    # parse initial crate places in stacks
    for j in range(len(stack_lines) - 1):
        line = stack_lines[j]
        print('Parse line:', line)
        stack_num = 0
        for i in range(1, len(stack_lines[0]), 4):
            if line[i] != ' ':
                stacks[stack_num].appendleft(line[i])
            stack_num += 1

    # move crates with instructions
    for instruction in f.read().split('\n'):
        instruction_data = instruction.split()
        stack_from = int(instruction_data[3]) - 1
        stack_to = int(instruction_data[5]) - 1
        temp = deque()
        for _ in range(int(instruction_data[1])):
            temp.appendleft(stacks[stack_from].pop())
        stacks[stack_to].extend(temp)

    result = ''
    for stack in stacks:
        result += stack.pop()
    print(result)
