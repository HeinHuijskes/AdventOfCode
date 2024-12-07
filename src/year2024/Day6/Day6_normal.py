import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day
from PythonFramework.Algorithms import *
import time


class Day6(Day):
    # Up, right, down, left
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    pointers = ['^', '>', 'v', '<']

    def parse(self, data):
        grid = [[char for char in line] for line in data]
        guard = [(x,y) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == "^"][0]
        return guard, grid

    def getGuardRoute(self, data):
        (x, y), grid = data
        dir_index = 0
        x_dir, y_dir = self.directions[dir_index]

        while True:
            grid[y][x] = self.pointers[dir_index]

            if not (0 < x < len(grid[0])-1) or not (0 < y < len(grid)-1):
                return grid

            if grid[y+y_dir][x+x_dir] == '#':
                dir_index = (dir_index + 1) % 4
                x_dir, y_dir = self.directions[dir_index]

            x, y = x+x_dir, y+y_dir

    def hasLoop(self, x, y, g, x_obs, y_obs):
        grid = [[a for a in b] for b in g]
        dir_index = 0
        x_dir, y_dir = self.directions[dir_index]
        visited = []
        grid[y_obs][x_obs] = '#'

        while True:
            if not (0 < x < len(grid[0])-1) or not (0 < y < len(grid)-1):
                return False

            while grid[y+y_dir][x+x_dir] == '#':

                if x_dir == 0 and y_dir == -1:
                    if (x, y) in visited:
                        return True
                    visited.append((x, y))

                dir_index = (dir_index + 1) % 4
                x_dir, y_dir = self.directions[dir_index]

            x, y = x+x_dir, y+y_dir

    def solvePartOne(self, data):
        grid = self.getGuardRoute(data)
        return sum([sum([t in self.pointers for t in line]) for line in grid])

    def solvePartTwo(self, data):
        (gx, gy), _ = data
        grid = self.getGuardRoute(data)
        route_coords = [(x,y) for y, c in enumerate(grid) for x, r in enumerate(c) if r in self.pointers and not (x == gx and y == gy)]
        return sum([self.hasLoop(gx, gy, grid, x, y) for (x, y) in route_coords])

Day6(6).getResult()
