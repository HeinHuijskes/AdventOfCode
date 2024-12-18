import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day


class Day3(Day):
    def solvePartOne(self, data):
        wires = data[0].split(',')[:-1], data[1].split(',')[:-1]
        visited = dict()
        intersects = []

        x, y = 0, 0
        for instruction in wires[0]:
            direction = instruction[0]
            if direction == 'U':
                for i in range(y, y + int(instruction[1:])):
                    y = i
                    visited[(x, y)] = True

            if direction == 'D':
                for i in range(y - int(instruction[1:]), y):
                    y = i
                    visited[(x, y)] = True

            if direction == 'L':
                for i in range(x - int(instruction[1:]), x):
                    x = i
                    visited[(x, y)] = True

            if direction == 'R':
                for i in range(x, x + int(instruction[1:])):
                    x = i
                    visited[(x, y)] = True

        x, y = 0, 0
        for instruction in wires[1]:
            direction = instruction[0]
            if direction == 'U':
                for i in range(y, y + int(instruction[1:])):
                    y = i
                    if (x, y) in visited:
                        intersects.append((x, y))

            if direction == 'D':
                for i in range(y - int(instruction[1:]), y):
                    y = i
                    if (x, y) in visited:
                        intersects.append((x, y))

            if direction == 'L':
                for i in range(x - int(instruction[1:]), x):
                    x = i
                    if (x, y) in visited:
                        intersects.append((x, y))

            if direction == 'R':
                for i in range(x, x + int(instruction[1:])):
                    x = i
                    if (x, y) in visited:
                        intersects.append((x, y))

        best = 999999999999999
        for intersect in intersects:
            x, y = abs(intersect[0]), abs(intersect[1])
            if x + y < best and (x != 0 or y != 0):
                best = x + y

        return best

    def solvePartTwo(self, data):
        return 'No part 2 solution yet'


Day3().getResult()
