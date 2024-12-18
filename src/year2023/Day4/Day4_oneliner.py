import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day


class Day4(Day):
    def solvePartOne(self, data):
        return sum([2**(b-1) for b in [len(a.intersection(b)) for a, b in [[set([a for a in s.split(' ') if a != '']) for s in l.split(': ')[1].split(' | ')] for l in data]] if b > 0])

    def solvePartTwo(self, data):
        return 'No implementation yet'


Day4().getResult()
