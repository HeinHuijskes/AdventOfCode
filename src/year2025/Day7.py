from src.PythonFramework.Day import Day
import src.PythonFramework.Algorithms as algs


class Solver(Day):
    test_answers = [21, 40]
    answers = [1594, 15650261281478]
    test = True

    def solve(self, data):
        start, lines = data[0].index('S'), [[char == '^' for char in data[i]] for i in range(0, len(data), 2)]
        beams = [[1 if i == start else 0 for i in range(len(lines[0]))]]
        splits = 0
        for line in lines[1:]:
            beams.append([])
            for i in range(len(line)):
                beam = beams[-2][i] if not line[i] else 0
                splits += line[i] and beams[-2][i] > 0
                if i > 0: 
                    beam += beams[-2][i-1] if line[i-1] else 0
                if i < len(line)-1: 
                    beam += beams[-2][i+1] if line[i+1] else 0
                beams[-1].append(beam)
        return splits, sum(beams[-1])

    def solvePartOne(self, data):
        return self.solve(data)[0]

    def solvePartTwo(self, data):
        return self.solve(data)[1]