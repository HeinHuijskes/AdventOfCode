from src.PythonFramework.Day import Day

import math


class Day8(Day):
    def parse(self, data):
        antennae = {}
        for y, line in enumerate(data):
            for x, char in enumerate(line):
                if char == '.':
                    continue
                if not char in antennae:
                    antennae[char] = []
                antennae[char].append((x,y))
        return antennae, (len(data[0]), len(data))
    
    def drawNodes(self, types, nodes, dimensions):
        x_dim, y_dim = dimensions
        grid = [['.' for x in range(x_dim)] for y in range(y_dim)]
        for x, y in nodes:
            grid[y][x] = '#'
        for type in types:
            antennae = types[type]
            for x, y in antennae:
                grid[y][x] = f'{type}'
        print('\n'.join([''.join(line) for line in grid]))

    def findAntinodes(self, antenna1, antenna2):
        (x1, y1), (x2, y2) = antenna1, antenna2
        dx, dy = x2-x1, y2-y1
        return (x1+2*dx, y1+2*dy), (x1-dx, y1-dy)
    
    def findAllAntinodes(self, antenna1, antenna2, x_lim, y_lim):
        (x1, y1), (x2, y2) = antenna1, antenna2
        dx, dy = x2-x1, y2-y1
        r = max(math.ceil((x_lim-x1)/abs(dx)), math.ceil((y_lim-y1)/abs(dy)))+1
        results = [(x1+i*dx, y1+i*dy) for i in range(r)]
        r = max(math.ceil(x1/abs(dx)), math.ceil(y1/abs(dy)))+1
        results += [(x1-i*dx, y1-i*dy) for i in range(r)]
        return results

    def solvePartOne(self, data):
        types, (x_lim, y_lim) = data
        antinodes = set()
        for symbol in types:
            antennea = types[symbol]
            for i, antenna1 in enumerate(antennea[:-1]):
                for antenna2 in antennea[i+1:]:
                    (x1, y1), (x2, y2) = self.findAntinodes(antenna1, antenna2)
                    if 0 <= x1 < x_lim and 0 <= y1 < y_lim:
                        antinodes.add((x1, y1))
                    if 0 <= x2 < x_lim and 0 <= y2 < y_lim:
                        antinodes.add((x2, y2))
        # self.drawNodes(types, antinodes, (x_lim, y_lim))
        return len(antinodes)

    def solvePartTwo(self, data):
        types, (x_lim, y_lim) = data
        antinodes = set()
        for symbol in types:
            antennea = types[symbol]
            for i, antenna1 in enumerate(antennea[:-1]):
                for antenna2 in antennea[i+1:]:
                    nodes = self.findAllAntinodes(antenna1, antenna2, x_lim, y_lim)
                    for x, y in nodes:
                        if 0 <= x < x_lim and 0 <= y < y_lim:
                            antinodes.add((x,y))
        # self.drawNodes(types, antinodes, (x_lim, y_lim))
        return len(antinodes)
