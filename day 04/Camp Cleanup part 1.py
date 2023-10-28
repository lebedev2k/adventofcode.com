with open('input.txt') as f:
    pairs = f.read().split('\n')
    counter = 0
    for line in pairs:
        pair1, pair2 = line.split(',')
        a, b = map(int, pair1.split('-'))
        c, d = map(int, pair2.split('-'))
        if (a >= c and b <= d) or (c >= a and d <= b):
            counter += 1

    print(counter)
