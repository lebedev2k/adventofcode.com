with open('day 08\input.txt') as f:
    data = []
    lines = f.read().split('\n')
    for line in lines:
        data.append(list(map(int, list(line))))
    
    max_score = 0
    for i in range(1, len(data)-1):
        for j in range(1, len(data[0])-1):
            score = 1
            steps = 1 #предлагаем сделать 1 шаг
            edge = len(data[0])-1
            #считаем score вправо
            while (j+steps)<=edge:
                if data[i][j+steps]>=data[i][j]:
                    steps += 1
                    break
                else:
                    steps += 1
            #если 1 шагов в одну из сторон, то score=0 и другие стороны можно уже не смотреть
            if steps==1: 
                continue
            score *= steps-1
            
            steps = -1
            edge = 0
            #считаем score влево
            while (j+steps)>=edge:
                if data[i][j+steps]>=data[i][j]:
                    steps -= 1
                    break
                else:
                    steps -= 1
            #если 0 шагов в одну из сторон, то score=0 и другие стороны можно уже не смотреть
            if steps==-1: 
                continue
            score *= abs(steps)-1
            
            steps = 1
            edge = len(data)-1
            #считаем score вниз
            while (i+steps)<=edge:
                if data[i+steps][j]>=data[i][j]:
                    steps += 1
                    break
                else:
                    steps += 1
            #если 1 шагов в одну из сторон, то score=0 и другие стороны можно уже не смотреть
            if steps==1: 
                continue
            score *= steps-1
            
            steps = -1
            edge = 0
            #считаем score вверх
            while (i+steps)>=edge:
                if data[i+steps][j]>=data[i][j]:
                    steps -= 1
                    break
                else:
                    steps -= 1
            #если 0 шагов в одну из сторон, то score=0 и другие стороны можно уже не смотреть
            if steps==-1: 
                continue
            score *= abs(steps)-1
            
            if score>max_score:
                max_score = score
                
    print(max_score)
            