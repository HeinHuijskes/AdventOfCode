import sys
sys.path.append('../../src')

from functools import reduce
from math import gcd

from PythonFramework.Day import Day


def lcm(n):
    return reduce((lambda x, y: int(x * y / gcd(x, y))), n)


class Day8(Day):
    def solvePartOne(self, data):
        sequence = [0 if x == 'L' else 1 for x in data[0]]
        lookup = {}
        for line in data[2:]:
            lookup[line[0:3]] = (line[7:10], line[12:15])
        node = 'AAA'
        goal = 'ZZZ'
        steps = 0
        while node != goal:
            for rl in sequence:
                steps += 1
                node = lookup[node][rl]
                if node == goal:
                    break
        return steps

    def solvePartTwo(self, data):
        sequence = [0 if x == 'L' else 1 for x in data[0]]
        lookup = {}
        for line in data[2:]:
            lookup[line[0:3]] = (line[7:10], line[12:15])
        nodes = [node[0:3] for node in data[2:] if node[2] == 'A']

        cycles = []
        for node in nodes:
            steps = 0
            while node[2] != 'Z':
                for rl in sequence:
                    steps += 1
                    node = lookup[node][rl]
                    if node[2] == 'Z':
                        break
            cycles.append(steps)

        return lcm(cycles)


Day8(8).getResult()
