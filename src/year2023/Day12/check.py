with open('mine.txt') as f:
    mine = f.read().split('\n')
    with open('controle.txt') as g:
        test = g.read().split('\n')
        for i in range(len(mine)):
            if mine[i] != test[i]:
                print(f'{i+1}: {mine[i]} should be {test[i]}')
