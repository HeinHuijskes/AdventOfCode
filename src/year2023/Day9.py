import sys
sys.path.append('../../src')

from PythonFramework.Day import Day


def extrapolate(values):
    current = values[-1]
    if sum([x != 0 for x in current]) == 0:
        return values
    values.append([current[i+1] - x for i, x in enumerate(current) if i < len(current)-1])
    return extrapolate(values)


def predictNext(values):
    value = values[-2][-1]
    for vals in reversed(values[:-2]):
        value = vals[-1] + value
    return value


def predictPrevious(values):
    value = values[-2][0]
    for vals in reversed(values[:-2]):
        value = vals[0] - value
    return value


class Day9(Day):
    def solvePartOne(self, data):
        return sum([predictNext(extrapolate([[int(x) for x in line.split(' ')]])) for line in data])                    

    def solvePartTwo(self, data):
        return sum([predictPrevious(extrapolate([[int(x) for x in line.split(' ')]])) for line in data])     


Day9(9).getResult(testOnly=False)
