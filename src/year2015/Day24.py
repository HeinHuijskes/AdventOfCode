import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
from math import prod


class Solver(Day):
    def parse(self, data):
        return sorted([int(package) for package in data], reverse=True)
    
    def solve(self, data, goal):
        best = [1 for i in range(goal)]
        queue = [(0, [], data)]
        while len(queue) > 0:
            weight, group1, packages = queue.pop()
            if sum(group1) == goal:
                if len(group1) < len(best) or (len(group1) == len(best) and prod(group1) < prod(best)):
                    best = group1
                continue
            for i, package in enumerate(packages):
                if weight + package <= goal and len(group1)+1 <= len(best):
                    queue.append((weight + package, group1 + [package], packages[i+1:]))
        print(best)
        return prod(best)

    def solvePartOne(self, data):
        return self.solve(data, sum(data)//3)

    def solvePartTwo(self, data):
        return self.solve(data, sum(data)//4)


Solver(day=24).getResult(testOnly=False)
