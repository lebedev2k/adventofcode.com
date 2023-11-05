with open('day 08\input.txt') as f:
    data = []
    lines = f.read().split('\n')
    for line in lines:
        data.append(list(map(int, list(line))))
    n = len(data[0])*2+(len(data)-2)*2

    assert (n == (99+99+97+97)) #test parsing for success

    cells = set()
    #обход слева-направо, справа-налево
    for i in range(1, len(data)-1):
        max_value = data[i][0]
        # обход слева-направо
        for j in range(1, len(data[i])-1):
            if data[i][j] > max_value:
                cells.add((i, j))
                max_value = data[i][j]
        max_value = data[i][len(data[i])-1]
        # обход справа-налево
        for j in range(len(data[i])-1, 0, -1):
            if data[i][j] > max_value:
                cells.add((i, j))
                max_value = data[i][j]
    #обход сверху-вниз, снизу-вверх
    for j in range(1, len(data[0])-1):
        max_value = data[0][j]
        # обход сверху-вниз
        for i in range(1, len(data)-1):
            if data[i][j] > max_value:
                cells.add((i, j))
                max_value = data[i][j]
        max_value = data[len(data)-1][j]
        # обход снизу-вверх
        for i in range(len(data)-1, 0, -1):
            if data[i][j] > max_value:
                cells.add((i, j))
                max_value = data[i][j]

    print('Result =', n+len(cells))
