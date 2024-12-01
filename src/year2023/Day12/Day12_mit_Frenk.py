import sys
sys.path.append('src')
from PythonFramework.Day import Day
sys.path.append('src/year2023/Day12')


def recurseSpring():
    
    pass


class Day12(Day):
    def solvePartOne(self, data):
        for line in data:
            notations = line.split(' ')
            springs, numbers = notations[0], [int(x) for x in notations[1].split(',')]

            options = []
            length = len(springs)
            number = 0
            for i, char in enumerate(springs):
                # Continue looking when encountering a dot
                if char == ".":
                    continue
                # Prune this branch if there is not enough length left
                if length - i < len(numbers[number:]) + sum(numbers[number:]):
                    break

    def solvePartTwo(self, data):
        return 'No part 2 solution yet'


Day12(12).getResult(testOnly=False)
