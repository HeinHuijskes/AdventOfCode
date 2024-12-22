import sys
sys.path.append('../../src')

from PythonFramework.Day import Day


class Day6(Day):
    def solvePartOne(self, data):
        grid = []
        for i in range(0, 1000):
            grid.append([])
            for j in range(0, 1000):
                grid[i].append(False)
        for line in data:
            toggle = False
            if 'turn on' in line:
                newValue = True
                sq = 8
            if 'turn off' in line:
                newValue = False
                sq = 9
            if 'toggle' in line:
                sq = 7
                toggle = True
            (a,b), (c,d) = [[int(y) for y in x.split(',')] for x in line[sq:].split(' through ')]
            for x in range(a, c+1):
                for y in range(b, d+1):
                    if toggle:
                        grid[x][y] = not grid[x][y]
                    else:
                        grid[x][y] = newValue
        return sum([sum(row) for row in grid])

    def solvePartTwo(self, data):
        grid = []
        for i in range(0, 1000):
            grid.append([])
            for j in range(0, 1000):
                grid[i].append(0)
        for line in data:
            if 'turn on' in line:
                value = 1
                sq = 8
            if 'turn off' in line:
                value = -1
                sq = 9
            if 'toggle' in line:
                sq = 7
                value = 2
            (a,b), (c,d) = [[int(y) for y in x.split(',')] for x in line[sq:].split(' through ')]
            for x in range(a, c+1):
                for y in range(b, d+1):
                    grid[x][y] = max(0, value + grid[x][y])
        return sum([sum(row) for row in grid])


Day6(6).getResult(testOnly=False)
