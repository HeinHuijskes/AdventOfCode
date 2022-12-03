def getResult():
    data = open('data.txt', 'r').read().split('\n')[:-1]
    print(solvePartOne(data))
    print(solvePartTwo(data))


def solvePartOne(data):
    c = [ord(set(x[len(x)//2:]).intersection(set(x[:len(x)//2])).pop()) - 96 for x in data]
    return sum([(lambda x: x if x > 0 else x + 58)(x) for x in c])


def solvePartTwo(d):
    f = lambda i: ord(set(d[i]).intersection(set(d[i + 1]), set(d[i + 2])).pop()) - 96 if i % 3 == 0 else 0
    return sum([(lambda x: x if x > -1 else x + 58)(x) for x in [f(i) for i in range(0, len(d))]])


getResult()
