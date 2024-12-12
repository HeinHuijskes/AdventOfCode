import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day
from PythonFramework.Algorithms import *


class Day12(Day):
    cardinal_directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def pad(self, grid, value):
        new_grid = [[value for i in range(len(grid[0])+2)] for j in range(len(grid)+2)]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                new_grid[y+1][x+1] = grid[y][x]
        return new_grid

    def parse(self, data):
        return self.pad([[char for char in line] for line in data], 0)

    def isNeighbour(self, x, y, x2, y2):
        return ((x == x2+1 or x == x2-1) and y == y2) or (x == x2 and (y == y2-1 or y == y2+1))
    
    def getNeighbours(self, x, y, visited, regions):
        neighbours = []
        for x2, y2 in regions:
            if (x2, y2) not in visited and self.isNeighbour(x, y, x2, y2):
                neighbours.append((x2, y2))
        return neighbours
    
    def getNeighbours(self, x, y, visited, grid):
        neighbours = []
        value = grid[y][x]
        for x_add, y_add in self.cardinal_directions:
            x_val, y_val = x+x_add, y+y_add
            if not visited[y_val][x_val] and grid[y_val][x_val] == value:
                neighbours.append((x_val, y_val))
                visited[y_val][x_val] = True
        return neighbours

    def getRegion(self, x, y, grid, visited):
        result = [(x, y)]
        visited[y][x] = True
        i = 0
        while i < len(result):
            x, y = result[i]
            result += self.getNeighbours(x, y, visited, grid)
            i += 1
        return result

    def getPerimeterLength(self, region, grid):
        result = 0
        for x, y in region:
            value = grid[y][x]
            result += 4
            for direction in self.cardinal_directions:
                if grid[y+direction[1]][x+direction[0]] == value:
                    result -= 1
        return result
    
    def findCorners(self, region, max_x, max_y):
        grid = [[False for j in range(max_x)] for i in range(max_y)]
        for x, y in region:
            grid[y][x] = True

        corners = 0
        for x in range(max_x-1):
            for y in range(max_y-1):
                # TL, TR, BL, BR
                kernel = [grid[y][x],   grid[y][x+1], 
                          grid[y+1][x], grid[y+1][x+1]]
                tiles = sum(kernel)
                if tiles != 0 and tiles != 4:
                    if tiles == 1 or tiles == 3:
                        corners += 1
                    elif tiles == 2:
                        if (kernel[0] and kernel[3]) or (kernel[1] and kernel[2]):
                            corners += 2
        return corners

    def solvePartOne(self, data):
        result = 0
        visited = [[val == 0 for val in line] for line in data]
        for y, line in enumerate(data):
            for x, value in enumerate(line):
                if visited[y][x]:
                    continue
                region = self.getRegion(x, y, data, visited)
                area = len(region)
                perimeter = self.getPerimeterLength(region, data)
                result += area * perimeter
        return result

    def solvePartTwo(self, data):
        result = 0
        max_x = len(data[0])
        max_y = len(data)
        visited = [[val == 0 for val in line] for line in data]
        for y, line in enumerate(data):
            for x, value in enumerate(line):
                if visited[y][x]:
                    continue
                region = self.getRegion(x, y, data, visited)
                area = len(region)
                perimeter = self.findCorners(region, max_x, max_y)
                result += area * perimeter
        return result


Day12().getResult(testOnly=False)
