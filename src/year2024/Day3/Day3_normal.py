import sys
import re
sys.path.append('../../../src')

from PythonFramework.Day import Day


class Day3(Day):
    def solvePartOne(self, data):
        numbers = []
        line = ''.join(data)
        mults = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
        numbers = [[int(y) for y in x[4:-1].split(',')] for x in mults]
        return sum([nr[0]*nr[1] for nr in numbers])

    def solvePartTwo(self, data):
        numbers = []
        do = True
        for instruction in re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", ''.join(data)):
            if instruction[:2] == "do":
                do = instruction == "do()"
            elif do:
                numbers += [[int(y) for y in instruction[4:-1].split(',')]]
        return sum([nr[0]*nr[1] for nr in numbers])


Day3(3).getResult()
