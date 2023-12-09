import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day


class Day2(Day):
    def solvePartOne(self, data):
        return sum([2*a*b+2*b*c+2*c*a+min(a*b,b*c,c*a) for a,b,c in [[int(x) for x in line.split('x')] for line in data]])

    def solvePartTwo(self, data):
        return sum([a*b*c+a*2+b*2+c*2-max(a,b,c)*2 for a,b,c in [[int(x) for x in line.split('x')] for line in data]])


Day2().getResult()
