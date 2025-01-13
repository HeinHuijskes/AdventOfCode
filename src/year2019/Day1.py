from src.PythonFramework.Day import Day


class Solver(Day):
    def solvePartOne(self, data):
        return sum([int(x)//3-2 for x in data])

    def solvePartTwo(self, data):
        fuel = [[int(x)//3-2] for x in data]
        map(fuel.append, fuel)
        for f in fuel:
            while f[-1]//3-2 > 0:
                f.append(f[-1]//3-2)
        return sum([sum(f) for f in fuel])
