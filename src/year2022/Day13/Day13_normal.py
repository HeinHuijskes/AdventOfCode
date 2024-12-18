from src.PythonFramework.Day import Day


class Day13(Day):

    def parse(self, data):
        packets = []
        for i in range(len(data)):
            if i + 1 % 3 == 0:
                continue
            line = data[i].split(',')
            packet = []
            level = 0
            for char in line:
                if char == '[':
                    level += 1
                elif char == ']':
                    level -= 1
                    continue
                else:
                    pass

        return data

    def checkOrder(self, first, second):
        return first

    def solvePartOne(self, data):
        return 'No part 1 solution yet'

    def solvePartTwo(self, data):
        return 'No part 2 solution yet'


Day13().getResult()
