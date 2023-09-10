with open('day 1//input.txt') as f:
    m0 = 0
    res = []
    for c in f:
        if c.strip()!='':
            m0 += int(c)
        else:
            res.append(m0)
            m0 = 0
    m = sorted(res)
    print(sum(m[-3:]))
    