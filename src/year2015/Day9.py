import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Day9(Day):
    def parse(self, data):
        travels = {}
        for line in data:
            city1, rest = line.split(' to ')
            city2, distance = rest.split(' = ')
            if city1 not in travels:
                travels[city1] = {}
            if city2 not in travels:
                travels[city2] = {}
            travels[city1][city2] = int(distance)
            travels[city2][city1] = int(distance)
        return travels
    
    def checkDistance(self, data, part2=False):
        length = len(data)
        queue = [(0, [travel]) for travel in data]
        compare_distance = None
        while len(queue) > 0:
            distance, cities = queue.pop()
            if len(cities) == length:
                if compare_distance == None or (not part2 and distance < compare_distance) or (part2 and distance > compare_distance):
                    compare_distance = distance
                continue
            city1 = cities[-1]
            for city2 in data[city1]:
                new_distance = distance+data[city1][city2]
                if city2 not in cities and (compare_distance == None or (not part2 and compare_distance > new_distance) or (part2 and distance < compare_distance)):
                    queue.append((distance+data[city1][city2], cities+[city2]))
        return compare_distance

    def solvePartOne(self, data):
        return self.checkDistance(data)

    def solvePartTwo(self, data):
        return self.checkDistance(data, part2=True)


Day9(9).getResult(testOnly=False)
