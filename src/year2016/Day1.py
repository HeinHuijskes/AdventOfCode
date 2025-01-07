import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Solver(Day):
    directions = {0: (0, -1), 90: (1, 0), 180: (0, 1), 270: (-1, 0)}
    dirs = {'L': 270, 'R': 90}
    def parse(self, data):
        return [(x[0], int(x[1:])) for x in data[0].split(', ')]

    def solvePartOne(self, data):
        x, y, direction = 0, 0, 0
        for dir, amount in data:
            direction = (direction + self.dirs[dir]) % 360
            x += amount * self.directions[direction][0]
            y += amount * self.directions[direction][1]
        return abs(x)+abs(y)

    def solvePartTwo(self, data):
        x, y, direction = 0, 0, 0
        positions = [(x, y)]
        for dir, amount in data:
            direction = (direction + self.dirs[dir]) % 360
            for i in range(amount):
                x += self.directions[direction][0]
                y += self.directions[direction][1]
                if (x, y) in positions:
                    return abs(x)+abs(y)
                else:
                    positions.append((x, y))


Solver(day=1).getResult(testOnly=False)
