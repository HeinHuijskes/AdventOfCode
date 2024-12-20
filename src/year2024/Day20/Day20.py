import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Day20(Day):
    def parse(self, data):
        start = [(x, y) for y, line in enumerate(data) for x, val in enumerate(line) if val == 'S'][0]
        goal = [(x, y) for y, line in enumerate(data) for x, val in enumerate(line) if val == 'E'][0]
        grid = [[False if char == '#' else True for char in line] for line in data]
        return grid, start, goal
    
    def getNeighbourCircle(self, cx, cy, grid, r):
        # Return all tiles that are not walls that are within radius r from (cx, cy) based on manhattan distance
        lim_x, lim_y = len(grid[0]), len(grid)
        return [(x,y) for x in range(cx-r, cx+r) for y in range(cy-r, cy+r) 
                if 0 <= x < lim_x and 0 <= y < lim_y and abs(x-cx) + abs(y-cy) < r and grid[y][x]]
    
    def solve(self, data, r):
        grid, (sx, sy), (gx, gy) = data
        path = algs.dijkstra(grid, sx, sy, gx, gy)
        path_grid = [[val for val in line] for line in grid]
        for x, y, score in path:
            path_grid[y][x] = score
        cheats = []
        for (x, y, score) in path:
            for nx, ny in self.getNeighbourCircle(x, y, grid, r=r):
                manhattan = (abs(x-nx) + abs(y-ny))
                new_score = path_grid[ny][nx]
                if new_score - manhattan > score:
                    cheats.append(new_score - score - manhattan)
        return sum([cheat >= 100 for cheat in cheats])

    def solvePartOne(self, data):
        return self.solve(data, r=3)

    def solvePartTwo(self, data):
        return self.solve(data, r=21)


Day20().getResult(testOnly=False)
