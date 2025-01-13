from src.PythonFramework.Day import Day


class Day10(Day):
    def findNeighbours(self, heights, x, y, val):
        neighbours = []
        if 0 < x and heights[y][x-1] == val + 1:
            neighbours.append((x-1, y))
        if x < len(heights)-1 and heights[y][x+1] == val + 1:
            neighbours.append((x+1, y))
        if 0 < y and heights[y-1][x] == val + 1:
            neighbours.append((x, y-1))
        if y < len(heights)-1 and heights[y+1][x] == val + 1:
            neighbours.append((x, y+1))
        return neighbours

    def parse(self, data):
        heights = [[int(x) for x in line] for line in data]
        zeroes = []
        height_map = []
        for y, line in enumerate(heights):
            new_line = []
            for x, val in enumerate(line):
                if val == 0:
                    zeroes.append((x,y))
                neighbours = self.findNeighbours(heights, x, y, val)
                new_line.append(neighbours)
            height_map.append(new_line)
        return height_map, zeroes
    
    def recurseNeighbours(self, height_map, level, x, y):
        if level == 9:
            return [(x, y)]
        
        level += 1
        neighbours = height_map[y][x]
        result = []
        for nx, ny in neighbours:
            result += self.recurseNeighbours(height_map, level, nx, ny)
        return result

    def solvePartOne(self, data):
        height_map, zeroes = data
        result = 0
        for x, y in zeroes:
            result += len(set(self.recurseNeighbours(height_map, 0, x, y)))
        return result

    def solvePartTwo(self, data):
        height_map, zeroes = data
        result = 0
        for x, y in zeroes:
            result += len(self.recurseNeighbours(height_map, 0, x, y))
        return result


Day10(10).getResults(testOnly=False)
