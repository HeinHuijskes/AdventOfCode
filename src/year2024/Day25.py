import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Day25(Day):
    def parse(self, data):
        locks, keys = [], []
        for i in range(0, len(data), 8):
            lengths = [sum([line[j] == '#' for line in data[i+1:i+6]]) for j in range(5)]
            if data[i] == '#####':
                locks.append(lengths)
            else:
                keys.append(lengths)
        return locks, keys

    def solvePartOne(self, data):
        locks, keys = data
        combinations = 0
        for lock in locks:
            for key in keys:
                fits = True
                for i in range(5):
                    if lock[i] + key[i] > 5:
                        fits = False
                        break
                combinations += fits
        return combinations

    def solvePartTwo(self, data):
        return 'No part 2 solution yet'


Day25(25).getResult(testOnly=False)
