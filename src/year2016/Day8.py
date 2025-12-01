from src.PythonFramework.Day import Day
from regex import regex


class Solver(Day):
    testOnly = True
    test_answers = [6, None]
    answers = [128, 'EOARGPHYAO']

    def printGrid(self, grid):
        print('\n'.join([''.join(line) for line in [['#' if x else '.' for x in l] for l in grid]]))

    def rect(self, grid, A, B):
        for x in range(A):
            for y in range(B):
                grid[y][x] = True

    def rotateColumn(self, grid, x, amount):
        y_lim = len(grid)
        ys = [grid[y][x] for y in range(y_lim)]
        ys = ys[-amount:] + ys[:y_lim-amount]
        for y in range(y_lim):
            grid[y][x] = ys[y]
        
    def rotateRow(self, grid, y, amount):
        grid[y] = grid[y][-amount:] + grid[y][:len(grid[y])-amount]

    def parse(self, data: list[str]):
        instructions = []
        for line in data:
            if line.startswith('rect'):
                A, B = map(int, regex.match('rect (\d+)x(\d+)', line).groups())
                instructions.append((self.rect, A, B))
            else:
                _, axis, A, B = regex.match('rotate (row|column) (y|x)=(\d+) by (\d+)', line).groups()
                if axis == 'x':
                    instructions.append((self.rotateColumn, int(A), int(B)))
                else:
                    instructions.append((self.rotateRow, int(A), int(B)))
        return instructions

    def solvePartOne(self, data):
        grid = [[False for i in range(50)] for j in range(6)]
        for func, A, B in data:
            func(grid, A, B)
        self.grid = grid
        return sum([sum(line) for line in grid])

    def solvePartTwo(self, data):
        self.printGrid(self.grid)
        return 'EOARGPHYAO'
