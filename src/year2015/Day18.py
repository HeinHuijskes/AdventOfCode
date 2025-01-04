import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Day18(Day):
    neighbour_range = [-1, 0, 1]
    def parse(self, data):
        grid = algs.gridify(data, '.')
        return grid
    
    def printGrid(self, grid):
        print('\n'.join([''.join(['#' if char else ' ' for char in line]) for line in grid]))
        print('-----------------')
    
    def getNeighboursOn(self, grid, x, y):
        lim_x, lim_y = len(grid[0]), len(grid)
        neighbours = 0
        for dx in self.neighbour_range:
            for dy in self.neighbour_range:
                if 0 <= x+dx < lim_x and 0 <= y+dy < lim_y and not (dx == 0 and dy == 0):
                    neighbours += grid[y+dy][x+dx]
        return neighbours
    
    def updateGrid(self, grid):
        new_grid = []
        for y, line in enumerate(grid):
            new_grid.append([])
            for x, tile in enumerate(line):
                neighbours = self.getNeighboursOn(grid, x, y)
                is_on = neighbours == 3 or (tile and neighbours == 2)
                new_grid[-1].append(is_on)
        return new_grid
    
    def turnOnCorners(self, grid):
        grid[0][0], grid[0][len(grid[0])-1], grid[len(grid)-1][0], grid[len(grid)-1][len(grid[0])-1] = True, True, True, True

    def solvePartOne(self, data):
        grid = data
        for i in range(100):
            grid = self.updateGrid(grid)
        return sum([sum(line) for line in grid])

    def solvePartTwo(self, data):
        grid = data
        self.turnOnCorners(grid)
        for i in range(100):
            grid = self.updateGrid(grid)
            self.turnOnCorners(grid)
        return sum([sum(line) for line in grid])


Day18(18).getResult(testOnly=False)
