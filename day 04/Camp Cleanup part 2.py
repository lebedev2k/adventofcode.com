with open('input.txt') as f:
    pairs = f.read().split('\n')
    counter = 0
    for line in pairs:
        pair1, pair2 = line.split(',')
        a, b = map(int, pair1.split('-'))
        c, d = map(int, pair2.split('-'))
        if b >= c and a <= d:
            counter += 1

    print(counter)
