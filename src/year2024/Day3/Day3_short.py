import sys
import re
sys.path.append('../../../src')

from PythonFramework.Day import Day


class Day3(Day):
    def solvePartOne(self, data):
        return sum([(lambda y: int(y[0])*int(y[1]))(x[4:-1].split(',')) for x in re.findall("mul\(\d{1,3},\d{1,3}\)", ''.join(data))])

    def solvePartTwo(self, data):
        # Use regex lookbehind to filter the string?
        return 'No part 2 solution yet'


Day3(3).getResult()
