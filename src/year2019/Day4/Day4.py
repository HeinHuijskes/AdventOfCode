import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day


class Day4(Day):
    def hasDouble(self, integer):
        integers = [int(x) for x in str(integer)]
        for i in range(0, len(integers)):
            number = integers[i]
            for j in range(i, len(integers)):
                if number == integers[j]:
                    return True
        return False

    def isIncreasing(self, integer):
        integers = [int(x) for x in str(integer)]
        for i in range(1, len(integers)):
            if integers[i] < integers[i-1]:
                return False
        return True

    def solvePartOne(self, data):
        range_values = data[0].split('-')
        a, b = int(range_values[0]), int(range_values[1])
        options = []
        for i in range(a, b+1):
            if self.hasDouble(i) and self.isIncreasing(i):
                options.append(i)

        return len(options)

    def solvePartTwo(self, data):
        return 'No part 2 solution yet'


Day4().getResult()
