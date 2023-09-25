with open('input.txt') as f:
    packs = f.read().split('\n')
    total_sum = 0

    for pack in packs:
        split_idx = len(pack)//2
        part1 = set(pack[0:split_idx])
        part2 = set(pack[split_idx:])
        for item in (part1 & part2):
            if ord(item)<91:
                total_sum += ord(item) - 38 #38 = ord('Z') - 52
            else:
                total_sum += ord(item) - 96 #96 = ord('z') - 26
    print(total_sum)



