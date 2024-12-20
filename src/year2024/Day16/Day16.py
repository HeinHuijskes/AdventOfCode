import sys
sys.path.append('../../../src')

import time

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Day16(Day):
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    def parse(self, data):
        grid = algs.gridify(data)
        reindeer = (1, len(grid)-2)
        goal = (len(grid[0])-2, 1)
        return grid, reindeer, goal

    def showPath(self, grid, path):
        directions = {(0, -1): '^', (1, 0): '>', (0, 1): 'v', (-1, 0): '<'}
        grid = [['#' if x else ' ' for x in line] for line in grid]
        for node in path.nodes:
            grid[node.y][node.x] = directions[(node.x_dir, node.y_dir)]
        print()
        print('\n'.join([''.join(line) for line in grid]))

    class Path:
        nodes = []
        cost = 0
        
        def __init__(self, nodes):
            self.nodes = [self.Node(node.x, node.y, node.x_dir, node.y_dir) for node in nodes]
        
        def visited(self, x, y, x_dir, y_dir):
            for node in self.nodes:
                if x_dir == node.x_dir and y_dir == node.y_dir and x == node.x and y == node.y:
                    return True
            return False
        
        def addNode(self, x, y, x_dir, y_dir):
            last_node = self.nodes[-1]
            if last_node.x_dir == x_dir and last_node.y_dir == y_dir:
                self.cost += 1
            else:
                self.cost += 1001
            self.nodes.append(self.Node(x, y, x_dir, y_dir))
        
        class Node:
            x, y, x_dir, y_dir = None, None, None, None
            
            def __init__(self, x, y, x_dir, y_dir, neighbours = []):
                self.x, self.y, self.x_dir, self.y_dir = x, y, x_dir, y_dir
                self.neighbours = neighbours

    # def binarySearch(self, paths, low, high, path):
    #     if high-low == 1:
    #         if paths[high].cost < path.cost:
    #             return high+1
    #         elif paths[low].cost > path.cost:
    #             return low
    #         else:
    #             return high
    #     mid = (high + low) // 2
    #     if paths[mid].cost > path.cost:
    #         return self.binarySearch(paths, low, mid - 1, path)
    #     else:
    #         return self.binarySearch(paths, mid + 1, high, path)
    
    def addPath(self, new_path, paths):
        for i, path in enumerate(paths):
            if new_path.cost < path.cost:
                paths.insert(i, new_path)
                return
        paths.append(new_path)
        # i = self.binarySearch(paths, 0, len(paths)-1, new_path)
    
    def getNeighbours(self, grid, x, y, x_dir, y_dir):
        neighbours = []
        for x_d, y_d in self.directions:
            if x_d*-1 == x_dir and y_d*-1 == y_dir:
                continue
            if grid[y+y_d][x+x_d]:
                neighbours.append((x+x_d, y+y_d, x_d, y_d))
        return neighbours

    def search(self, grid, reindeer, goal):
        (rx, ry), (gx, gy) = reindeer, goal
        x_dir, y_dir = (1, 0)
        paths = [self.Path([self.Path.Node(rx, ry, x_dir, y_dir)])]
        cheapest = [[{} for char in line] for line in grid]
        max_length = 0
        i = 0
        results = []

        while len(paths) > 0:
            i += 1
            path = paths.pop(0)
            length = len(path.nodes)
            # if length > max_length:
            #     max_length = length
            #     print(f'Path length: {len(path.nodes)}, {len(paths)}')
            # if i % 10000 == 0:
            #     print(f'Path length: {len(path.nodes), {i}}')
            # # self.showPath(grid, path)
            last_node = path.nodes[-1]
            if last_node.x == gx and last_node.y == gy:
                results.append(path)
                continue
            node  = path.nodes[-1]

            neighbours = self.getNeighbours(grid, node.x, node.y, node.x_dir, node.y_dir)
            # Precompute straight paths
            if len(neighbours) == 1:
                while True:
                    node = neighbours[0]
                    path.addNode(*node)
                    neighbours = self.getNeighbours(grid, *node)
                    last_node = path.nodes[-1]
                    if last_node.x == gx and last_node.y == gy:
                        results.append(path)
                        break
                    if len(neighbours) > 1 or len(neighbours) == 0 or (neighbours[0][0] == gx and neighbours[0][1] == gy):
                        break

            for x, y, x_dir, y_dir in neighbours:
                if path.visited(x, y, x_dir, y_dir):
                    continue
                extended_path = self.Path(path.nodes)
                extended_path.cost = path.cost
                extended_path.addNode(x, y, x_dir, y_dir)
                if not (x_dir, y_dir) in cheapest[y][x] or extended_path.cost <= cheapest[y][x][(x_dir, y_dir)]:
                    cheapest[y][x][(x_dir, y_dir)] = extended_path.cost
                else:
                    continue
                self.addPath(extended_path, paths)
        return results

    def solvePartOne(self, data):
        grid, reindeer, goal = data
        path = self.search(grid, reindeer, goal)[0]
        return path.cost

    def solvePartTwo(self, data):
        grid, reindeer, goal = data
        paths = self.search(grid, reindeer, goal)
        results = set()
        lowest = paths[0]
        for path in paths:
            if path.cost < lowest.cost:
                lowest = path
        # print(lowest.cost)
        paths = [path for path in paths if path.cost == lowest.cost]
        for path in paths:
            # print(path.cost)
            # self.showPath(grid, path)
            for node in path.nodes:
                results.add((node.x, node.y))
        return len(results)


Day16().getResult(testOnly=False)
