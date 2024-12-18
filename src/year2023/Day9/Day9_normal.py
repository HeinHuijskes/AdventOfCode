import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day


def extrapolate(values):
    current = values[-1]
    if sum([x != 0 for x in current]) == 0:
        return values
    result = [current[i+1] - x for i, x in enumerate(current) if i < len(current)-1]
    values.append(result)
    return extrapolate(values)


def displayValues(values):
    for i, value in enumerate(values):
        print(' '*i + ' '.join([str(x) for x in value]))


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
        predictions = []
        for line in data:
            values = [[int(x) for x in line.split(' ')]]
            values = extrapolate(values)
            prediction = predictNext(values)
            predictions.append(prediction)
            # displayValues(values)
            # print(prediction)
                    
        return sum(predictions)

    def solvePartTwo(self, data):
        predictions = []
        for line in data:
            values = [[int(x) for x in line.split(' ')]]
            values = extrapolate(values)
            prediction = predictPrevious(values)
            predictions.append(prediction)
            # displayValues(values)
            # print(prediction)
                    
        return sum(predictions)


Day9().getResult(testOnly=False)
