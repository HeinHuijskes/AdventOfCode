import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day

def getXMAS(grid, x, y):
    dim_x, dim_y = len(grid[0]), len(grid)
    xmas = 4
    # 8 possible directions to go from the inital X
    directions = [(0, 1), (1, 1), (1, 0), (-1, 0), (-1, -1), (0, -1), (-1, 1), (1, -1)]
    results = []
    for x_mult, y_mult in directions:
        # Check bounds for this direction
        if (0 <= (x + (xmas-1)*x_mult) < dim_x) and (0 <= (y + (xmas-1)*y_mult) < dim_y):
            # Find 4 letters in this direction and store them as a string
            results.append(''.join([grid[y+i*y_mult][x+i*x_mult] for i in range(xmas)]))
    return results

def getMAS(grid, x, y):
    dim_x, dim_y, = len(grid[0]), len(grid)
    # Easier bounds check
    if (0 < x < dim_x-1) and (0 < y < dim_y-1):
        # Easier letter finding: always take opposite corners around A
        return f'{grid[y-1][x-1]}{grid[y][x]}{grid[y+1][x+1]}', f'{grid[y-1][x+1]}{grid[y][x]}{grid[y+1][x-1]}'
    return None

class Day4(Day):
    def solvePartOne(self, data):
        grid = [[char for char in line] for line in data]
        total = 0
        for y, row in enumerate(grid):
            for x, c in enumerate(row):
                if c == "X":
                    # Gather all words starting from this X
                    words = getXMAS(grid, x, y)
                    total += sum([word == "XMAS" for word in words])
        return total

    def solvePartTwo(self, data):
        grid = [[char for char in line] for line in data]
        total = 0
        options = ["MAS", "SAM"]
        for y, row in enumerate(grid):
            for x, c in enumerate(row):
                if c == "A":
                    # Gather the 2 words in the X around this A
                    words = getMAS(grid, x, y)
                    if words:
                        # 'Boolean counting', so to say
                        total += words[0] in options and words[1] in options
        return total


Day4(4).getResult()
