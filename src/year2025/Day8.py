from src.PythonFramework.Day import Day
from math import sqrt, prod


class Solver(Day):
    test_answers = [40, 25272]
    answers = [133574, 2435100380]

    def parse(self, data: list[str]):
        return [tuple(int(x) for x in point.split(',')) for point in data]

    def solvePartOne(self, data):
        distance_map = {}
        for i in range(len(data)-1):
            for j in range(i+1, len(data)):
                (x1, y1, z1), (x2, y2, z2) = data[i], data[j]
                distance = sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
                distance_map[distance] = [i, j]
        self.circuits = [distance_map[dist] for dist in sorted(distance_map.keys())]
        circuits = self.circuits[:1000]

        change = True
        while change:
            change = False
            result = []

            while len(circuits) > 0:
                circuit1 = circuits.pop()

                for index, circuit2 in enumerate(circuits):
                    found = False
                    for point in circuit1:
                        if point in circuit2:
                            circuit1 = list(set(circuit1 + circuit2))
                            circuits.pop(index)
                            found = True
                            break
                    if found:
                        change = True
                        break
                
                result.append(circuit1)
            circuits = result
        return prod(sorted([len(circuit) for circuit in circuits])[-3:])

    def solvePartTwo(self, data):
        junctions = set()
        for point1, point2 in self.circuits:
            junctions.add(point1)
            junctions.add(point2)
            if len(junctions) >= len(data):
                break
        return data[point1][0] * data[point2][0]
