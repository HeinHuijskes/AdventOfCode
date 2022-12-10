import re as s


def getResult():
    data = open('data.txt', 'r').read().split('\n')[:-1]
    print(solvePartOne(data))
    print(solvePartTwo(data))


def solvePartOne(d):
    return sum([(lambda c: (c[0] <= c[2] and c[1] >= c[3]) or (c[0] >= c[2] and c[1] <= c[3]))(list(map(int, (s.split(',|-', c))))) for c in d])


def solvePartTwo(d):
    return sum([(lambda c: not (c[1] < c[2] or c[0] > c[3]))(list(map(int, (s.split(',|-', c))))) for c in d])


getResult()
