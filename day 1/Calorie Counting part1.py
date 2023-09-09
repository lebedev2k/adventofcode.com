with open('day 1//input.txt') as f:
    m = 0
    m0 = 0
    for c in f:
        if c.strip()!='':
            m0 += int(c)
        else:
            if m0 > m:
                m = m0
            m0 = 0
    print(m)