import sys
sys.path.append('../../src')

from PythonFramework.Day import Day


class Day3(Day):
    directions = {'^': (0, 1), '>': (1, 0), 'v': (0, -1), '<': (-1, 0)}
    def move(self, housemap, data):
        x, y = 0, 0
        for direction in data:
            i, j = self.directions[direction]
            x, y = x + i, y + j
            housemap[(x,y)] = True
        return housemap

    def solvePartOne(self, data):
        return len(self.move({}, data[0]))

    def solvePartTwo(self, data):
        santa_data = [x for i, x in enumerate(data[0]) if i % 2 == 0]
        robot_data = [x for i, x in enumerate(data[0]) if i % 2 == 1]
        housemap = self.move({}, santa_data)
        return len(self.move(housemap, robot_data))


Day3(3).getResult()
