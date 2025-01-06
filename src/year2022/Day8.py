import sys
sys.path.append('../../src')

from PythonFramework.Day import Day


class Solver(Day):
    def parse(self, data):
        grid = []
        for line in data:
            grid.append([])
            for char in line:
                grid[len(grid)-1].append(int(char))
        return grid

    def setupVisibleGrid(self, x, y):
        grid = []
        for i in range(0, y):
            grid.append([])
            for j in range(0, x):
                if 0 < j < x-1 and 0 < i < y-1:
                    grid[i].append(False)
                else:
                    grid[i].append(True)

        return grid

    def updateVisibleGrid(self, integer_grid, visible_grid):
        # Loop over only the inner part of the grid, not the sides
        for i in range(1, len(integer_grid)-1):
            high_right = integer_grid[i][len(integer_grid)-1]
            high_left = integer_grid[i][0]
            high_up = integer_grid[0][i]
            high_down = integer_grid[len(integer_grid)-1][i]

            for j in range(1, len(integer_grid)-1):
                x, y = j, i
                left = integer_grid[y][x]
                if left > high_left:
                    high_left = left
                    visible_grid[y][x] = True

                x, y = (len(integer_grid)-j-1), i
                right = integer_grid[y][x]
                if right > high_right:
                    high_right = right
                    visible_grid[y][x] = True

                x, y = i, j
                up = integer_grid[y][x]
                if up > high_up:
                    high_up = up
                    visible_grid[y][x] = True

                x, y = i, (len(integer_grid)-j-1)
                down = integer_grid[y][x]
                if down > high_down:
                    high_down = down
                    visible_grid[y][x] = True

    def getAmountOfVisibleTrees(self, visible_grid):
        amount = 0
        for line in visible_grid:
            amount += sum(line)
        return amount

    def getScenicScore(self, integer_grid, x, y):
        own_height = integer_grid[y][x]
        scores = [0, 0, 0, 0]
        # To the left
        for i in range(0, x):
            tree_height = integer_grid[y][x-1-i]
            scores[0] += 1
            if tree_height >= own_height:
                break
        # To the right
        for i in range(x, len(integer_grid)-1):
            tree_height = integer_grid[y][i+1]
            scores[1] += 1
            if tree_height >= own_height:
                break
        # Up
        for i in range(0, y):
            tree_height = integer_grid[y-1-i][x]
            scores[2] += 1
            if tree_height >= own_height:
                break
        # Down
        for i in range(y, len(integer_grid)-1):
            tree_height = integer_grid[i+1][x]
            scores[3] += 1
            if tree_height >= own_height:
                break
        scenic_score = 1
        for score in scores:
            scenic_score *= score
        return scenic_score

    def generateScenicScores(self, integer_grid):
        scenic_scores = []
        for y in range(0, len(integer_grid)):
            scenic_scores.append([])
            for x in range(0, len(integer_grid)):
                if 0 < y < len(integer_grid)-1 and 0 < x < len(integer_grid)-1:
                    scenic_scores[len(scenic_scores)-1].append(self.getScenicScore(integer_grid, x, y))
                else:
                    scenic_scores[len(scenic_scores)-1].append(0)
        return scenic_scores

    def findLargestScenicScore(self, score_grid):
        high_score = 0
        for line in score_grid:
            for score in line:
                if score > high_score:
                    high_score = score
        return high_score

    def solvePartOne(self, data):
        visible_grid = self.setupVisibleGrid(len(data[0]), len(data))
        self.updateVisibleGrid(data, visible_grid)
        return self.getAmountOfVisibleTrees(visible_grid)

    def solvePartTwo(self, data):
        scenic_grid = self.generateScenicScores(data)
        return self.findLargestScenicScore(scenic_grid)


Solver(day=8).getResult()
