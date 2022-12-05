import re as r


def getResult():
    data = open('data.txt', 'r').read().split('\n')[:-1]
    print(solvePartOne(data))
    print(solvePartTwo(data))


def solvePartOne(data):
    # Separate the instructions and the initial state of crates
    ins, ini = data[10:], data[:9]
    # Prepare an array to store the stacks of crates in
    cra = [[] for i in range(0, (len(ini[0])+1)//4)]
    # Parse the current state of crates and store in the stack
    [(lambda: cra[(x-1)//4].insert(0, ini[y][x]) if ini[y][x] != ' ' else 0)() for y in range(0, len(ini)) for x in range(1, len(ini[0]), 4)]
    # Parse the instructions and apply them to the stack
    [[cra[c-1].append(cra[b-1].pop()) for i in range(0, a)] for [a, b, c] in [[int(x) for x in r.findall(r'\d+', i)] for i in ins]]
    # Collect the top of each array in the stack
    return ''.join([c.pop() for c in cra])


def solvePartTwo(data):
    # Same as part 1
    ins, ini = data[10:], data[:9]
    cra = [[] for i in range(0, (len(ini[0])+1)//4)]
    [(lambda: cra[(x-1)//4].insert(0, ini[y][x]) if ini[y][x] != ' ' else 0)() for y in range(0, len(ini)) for x in range(1, len(ini[0]), 4)]
    # Same as part 1, but collect the boxes to a list first, and reverse it
    [[cra[c-1].append(box) for box in list(reversed([cra[b-1].pop() for i in range(0, a)]))] for [a, b, c] in [[int(x) for x in r.findall(r'\d+', i)] for i in ins]]
    return ''.join([c.pop() for c in cra])


getResult()
