import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day


class Day3(Day):
    def solvePartOne(self, data):
        housemap = {}
        directions = {'^': (0, 1), '>': (1, 0), 'v': (0, -1), '<': (-1, 0)}
        x, y = 0, 0
        for direction in data[0]:
            i, j = directions[direction]
            x, y = x + i, y + j
            if (x, y) in housemap.keys():
                housemap[(x,y)] += 1
            else:
                housemap[(x,y)] = 1
        return len(housemap.keys())

    def solvePartTwo(self, data):
        housemap = {}
        directions = {'^': (0, 1), '>': (1, 0), 'v': (0, -1), '<': (-1, 0)}
        s_x, s_y, r_x, r_y = 0, 0, 0, 0
        santasTurn = True
        for direction in data[0]:
            i, j = directions[direction]
            if santasTurn:
                x, y = s_x, s_y
            else:
                x, y = r_x, r_y
            x, y = x + i, y + j
            if (x, y) in housemap.keys():
                housemap[(x,y)] += 1
            else:
                housemap[(x,y)] = 1
                
            if santasTurn:
                s_x, s_y = x, y
            else:
                r_x, r_y = x, y
            santasTurn = not santasTurn
        return len(housemap.keys())


Day3().getResult()
