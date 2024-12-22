import sys
sys.path.append('../../src')

from PythonFramework.Day import Day


class Day1(Day):
    def solvePartOne(self, data):
        return sum([1 if x == '(' else -1 for x in data[0]])

    def solvePartTwo(self, data):
        moves = [1 if x == '(' else -1 for x in data[0]]
        result = 0
        for i, move in enumerate(moves):
            result += move
            if result < 0:
                break
        return i + 1


Day1(1).getResult()
