import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Day10(Day):
    def parse(self, data):
        return [int(x) for x in data[0]]
    
    def solve(self, data, iterations):
        for i in range(iterations):
            result = []
            j = 0
            while j < len(data):
                x = data[j]
                count = 1
                while j + count < len(data):
                    if data[j+count] != x:
                        break
                    count += 1
                result += [count, x]
                j += count
            data = result
        return len(data)

    def solvePartOne(self, data):
        return self.solve(data, 40)

    def solvePartTwo(self, data):
        return self.solve(data, 50)


Day10(10).getResult(testOnly=False)
