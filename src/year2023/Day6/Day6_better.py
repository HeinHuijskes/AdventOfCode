import sys
sys.path.append('../../../src')

import regex as re
import math

from PythonFramework.Day import Day


class Day6(Day):
    def solvePartOne(self, data):
        return 'No part 1 solution yet'

    def solvePartTwo(self, data):
        t = int(''.join(re.findall('\d', data[0])))
        d = int(''.join(re.findall('\d', data[1])))
        x_1 = (-t - math.sqrt(t**2-4*d))/-2
        x_2 = (-t + math.sqrt(t**2-4*d))/-2
        return math.ceil(x_1) - math.ceil(x_2)


Day6().getResult()
