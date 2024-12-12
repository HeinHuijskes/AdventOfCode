import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day
from PythonFramework.Algorithms import *


class Day12(Day):
    def parse(self, data):
        regions = {}
        for y, line in enumerate(data):
            for x, char in enumerate(line):
                if char not in regions:
                    regions[char] = []
                regions[char].append((x, y))
        return regions, data
    
    def isNeighbour(self, x, y, x2, y2):
        return ((x == x2+1 or x == x2-1) and y == y2) or (x == x2 and (y == y2-1 or y == y2+1))
    
    def getNeighbours(self, x, y, visited, regions):
        neighbours = []
        for x2, y2 in regions:
            if (x2, y2) not in visited and self.isNeighbour(x, y, x2, y2):
                neighbours.append((x2, y2))
        return neighbours

    def defineRegions(self, regions):
        result = []
        visited = []
        queue = []
        for x, y in regions:
            if (x, y) in visited:
                continue
            visited.append((x, y))
            queue.append((x, y))
            region = [(x, y)]
            while len(queue) > 0:
                x, y = queue.pop()
                neighbours = self.getNeighbours(x, y, visited, regions)
                queue += neighbours
                visited += neighbours
                region += neighbours
            result.append(region)

        return result
    
    def findPerimeter(self, region):
        result = 0
        for x, y in region:
            result += 4 - len(self.getNeighbours(x, y, [], region))
        return result
    
    def findCorners(self, region, max_x, max_y):
        # Pad with +2 to add a layer around the outside
        grid = [[False for j in range(max_x+2)] for i in range(max_y+2)]
        for x, y in region:
            # Pad x and y too
            grid[y+1][x+1] = True
        corners = 0

        for x in range(max_x+1):
            for y in range(max_y+1):
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
        data = data[0]
        for region in data:
            regions = data[region]
            regions = self.defineRegions(regions)
            for r in regions:
                area = len(r)
                perimeter = self.findPerimeter(r)
                print(region, area, perimeter)
                result += area * perimeter

        return result

    def solvePartTwo(self, data):
        result = 0
        data, grid = data
        max_x = len(grid[0])
        max_y = len(grid)
        for region in data:
            regions = data[region]
            regions = self.defineRegions(regions)
            for r in regions:
                area = len(r)
                sides = self.findCorners(r, max_x, max_y)
                result += area * sides

        return result


Day12().getResult(testOnly=False)
