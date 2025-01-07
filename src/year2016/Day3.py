import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
from regex import regex


class Solver(Day):
    def parse(self, data):
        return [[int(x) for x in regex.findall('(\d+)', line)] for line in data]

    def solvePartOne(self, data):
        result = 0
        for line in data:
            largest = line.pop(line.index(max(line)))
            result += largest < sum(line)
        return result

    def solvePartTwo(self, data):
        columns = []
        for i in range(3):
            columns += [[data[j+k][i] for k in range(3)] for j in range(0, len(data), 3)]
        result = 0
        for line in columns:
            largest = line.pop(line.index(max(line)))
            result += largest < sum(line)
        return result


Solver(day=3).getResult(testOnly=False)
