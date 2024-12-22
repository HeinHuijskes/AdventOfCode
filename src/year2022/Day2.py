def getResult():
    data = open('data.txt', 'r').read().split('\n')[:-1]
    print(solvePartOne(data))
    print(solvePartTwo(data))


def solvePartOne(data):
    options = {'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}
    return sum([(lambda c: options[c])(c) for c in data])


def solvePartTwo(data):
    options = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}
    return sum([(lambda c: options[c])(c) for c in data])


getResult()
