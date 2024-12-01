import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day


def transpose(array):
    result = [[y for y in range(len(array))] for x in range(len(array[0]))]
    for x, row in enumerate(array):
        for y, col in enumerate(row):
            result[y][x] = col
    return result


def comparePatternLines(line1, line2):
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            return False
        
    print(''.join(line1), ''.join(line2), 'The same!')
    return True


def checkDuplication(i, j, pattern):
    diff = j - i
    if diff >= 2:
        for k in range(1, 1+diff//2):
            if not comparePatternLines(pattern[i+k], pattern[j-k]):
                return False
    else:
        return False
    return True


def findDuplicates(pattern, secondAttempt = False):
    lines = None
    printPattern(pattern)
    for i in range(0, len(pattern)-1):
        for j in range(i+1, len(pattern)):
            if comparePatternLines(pattern[i], pattern[j]) and checkDuplication(i, j, pattern):
                # Found duplication
                lines = i + (j - i + 1) // 2
                break
        if lines != None:
            break
    if lines == None:
        if not secondAttempt:
            print('transposed!')
            return findDuplicates(transpose(pattern), True) // 100
        else:
            print('???')
    return 100 * lines


def printPattern(pattern):
    for line in pattern:
        print(''.join(line))


class Day13(Day):
    def solvePartOne(self, data):
        patterns = [x.split('-') for x in '-'.join(data).split('--')]
        result = 0
        for pattern in patterns:
            print(findDuplicates(pattern), pattern)
        return 'No part 1 solution yet'

    def solvePartTwo(self, data):
        return 'No part 2 solution yet'


Day13().getResult(testOnly=True)
