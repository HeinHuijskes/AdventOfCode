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
        result = 0
        for number in numbers:
            result += number[0] * number[1]
        return result

    def solvePartTwo(self, data):
        numbers = []
        do = True
        line = ''.join(data)
        mults = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
        numbers = []
        for mult in mults:
            if mult[:2] == "do":
                if mult == "do()":
                    do = True
                elif mult == "don't()":
                    do = False
                continue
            if do:
                numbers += [[int(y) for y in mult[4:-1].split(',')]]
        result = 0
        for number in numbers:
            result += number[0] * number[1]
        return result


Day3(3).getResult()
