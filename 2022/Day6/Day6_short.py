def getResult():
    data = open('data.txt', 'r').read().split('\n')[:-1]
    print(solvePartOne(data))
    print(solvePartTwo(data))


def solvePartOne(data):
    return [x for x in [i + 4 if (lambda c: (lambda f, *a: f(f, *a))(lambda rec, c: True if len(c) == 1 else (lambda fun, l: False if l[0] in l[1:] else fun(fun, l[1:]))(rec, c), c))(data[0][i:i + 4]) else 0 for i in range(0, len(data[0]))] if x != 0][0]


def solvePartTwo(data):
    return [x for x in [i + 14 if (lambda c: (lambda f, *a: f(f, *a))(lambda rec, c: True if len(c) == 1 else (lambda fun, l: False if l[0] in l[1:] else fun(fun, l[1:]))(rec, c), c))(data[0][i:i + 14]) else 0 for i in range(0, len(data[0]))] if x != 0][0]


getResult()
