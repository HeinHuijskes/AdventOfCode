import re as r


def getResult():
    data = open('data.txt', 'r').read().split('\n')[:-1]
    print(solvePartOne(data))
    print(solvePartTwo(data))


def solvePartOne(data):
    instructions, stackage = data[10:], data[:9]

    stacks = [[] for i in range(0, (len(stackage[0])+1)//4)]
    for x in range(1, len(stackage[0]), 4):
        for y in range(0, len(stackage)):
            if stackage[y][x] != ' ':
                stacks[(x-1)//4].insert(0, stackage[y][x])

    for instruction in instructions:
        [x, y, z] = [int(x) for x in r.findall(r'\d+', instruction)]
        for i in range(0, x):
            stacks[z-1].append(stacks[y-1].pop())

    return ''.join([s.pop() for s in stacks])


def solvePartTwo(data):
    # ADD SOLUTION BELOW
    return data[0]


getResult()
