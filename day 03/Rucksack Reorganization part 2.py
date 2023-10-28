with open('input2.txt') as f:
    packs = f.read().split('\n')

    total_sum = 0
    for i in range(0, len(packs), 3):
        for item in (set(packs[i]) & set(packs[i + 1]) & set(packs[i + 2])):
            if ord(item) < 91:
                total_sum += ord(item) - 38  # 38 = ord('Z') - 52
            else:
                total_sum += ord(item) - 96  # 96 = ord('z') - 26
    print(total_sum)
