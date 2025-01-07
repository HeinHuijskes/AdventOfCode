import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Solver(Day):
    directions = {'U': (0, -1), 'R': (1, 0), 'D': (0, 1), 'L': (-1, 0)}
    def parse(self, data):
        return [[self.directions[letter] for letter in line] for line in data]

    def solvePartOne(self, data):
        buttons = []
        x, y = 1, 1
        for line in data:
            for dx, dy in line:
                if 0 <= x+dx <= 2 and 0 <= y+dy <= 2:
                    x, y = x+dx, y+dy
            buttons.append(str((y)*3 + x+1))
        return ''.join(buttons)

    def solvePartTwo(self, data):
        layout = [[None, None, 1, None, None],[None, 2, 3, 4, None],[5, 6, 7, 8, 9],[None, 'A', 'B', 'C', None],[None, None, 'D', None, None]]
        buttons = []
        x, y = 0, 2
        for line in data:
            for dx, dy in line:
                if 0 <= x+dx <= 4 and 0 <= y+dy <= 4 and layout[y+dy][x+dx] != None:
                    x, y = x+dx, y+dy
            buttons.append(str(layout[y][x]))
        return ''.join(buttons)


Solver(day=2).getResult(testOnly=False)
