from src.PythonFramework.Day import Day
import src.PythonFramework.Algorithms as algs


class Solver(Day):
    test_answers = [13, 43]
    answers = [1604, 9397]
    test = True

    def parse(self, data: list[str]):
        return algs.padGrid([[cell == '@' for cell in row] for row in data], padding=False)
    
    def canAccess(self, sx, sy, grid):
        return 5 > sum([grid[y][x] for x in range(sx-1, sx+2) for y in range(sy-1, sy+2)])

    def solvePartOne(self, data):
        return sum([self.canAccess(x, y, data) for x in range(1, len(data[0])-1) for y in range(1, len(data)-1) if data[y][x]])

    def solvePartTwo(self, data):
        result = 1
        total = 0
        while result != 0:
            result = 0
            for x in range(1, len(data[0])-1):
                for y in range(1, len(data)-1):
                    if data[y][x] and self.canAccess(x, y, data):
                        result += 1
                        data[y][x] = False
            total += result
        return total
