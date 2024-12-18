import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day
from PythonFramework.Algorithms import *


class Day18(Day):
    def parseTest(self, data):
        return self.parse(data)[0], 6, 12

    def parse(self, data):
        byte_positions = [list(int(x) for x in line.split(',')) for line in data]
        return byte_positions, 70, 1024
    
    def displayGrid(self, grid, nodes):
        result = [[' ' if val else '#' for val in line] for line in grid]
        result = [[result[y][x] if val == None else 'O' for x, val in enumerate(line)] for y, line in enumerate(nodes)]
        print('\n'.join([''.join(line) for line in result]))
    
    def getNeighbours(self, grid, x, y, nodes):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        lim_x, lim_y = len(grid[0]), len(grid)
        return [(x+dx, y+dy) for dx, dy in directions if 0 <= x+dx < lim_x and 0 <= y+dy < lim_y and grid[y+dy][x+dx] and nodes[y+dy][x+dx] == None]
    
    def dijkstra(self, grid, x, y, gx, gy):
        nodes = [[None for i in range(len(grid[0]))] for j in range(len(grid))]
        nodes[y][x] = 0
        queue = [(x, y)]
        while (x != gx or y != gy) and len(queue) != 0:
            x, y = queue.pop(0)
            neighbours = self.getNeighbours(grid, x, y, nodes)
            for nx, ny in neighbours:
                queue.append((nx, ny))
                nodes[ny][nx] = nodes[y][x] + 1
        return nodes[y][x], (y == gy and x == gx)

    def solvePartOne(self, data):
        positions, dimension, sim_length = data
        grid = [[True for x in range(dimension+1)] for y in range(dimension+1)]
        for x, y in positions[:sim_length]:
            grid[y][x] = False
        return self.dijkstra(grid, 0, 0, dimension, dimension)[0]

    def solvePartTwo(self, data):
        positions, dimension, sim_length = data
        grid = [[True for x in range(dimension+1)] for y in range(dimension+1)]
        for x, y in positions[:sim_length]:
            grid[y][x] = False
        for x, y in positions[sim_length:]:
            grid[y][x] = False
            if not self.dijkstra(grid, 0, 0, dimension, dimension)[1]:
                return x, y


Day18().getResult(testOnly=False)
