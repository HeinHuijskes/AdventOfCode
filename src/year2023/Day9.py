from src.PythonFramework.Day import Day


class Solver(Day):
    def extrapolate(self, values):
        current = values[-1]
        if sum([x != 0 for x in current]) == 0:
            return values
        values.append([current[i+1] - x for i, x in enumerate(current) if i < len(current)-1])
        return self.extrapolate(values)

    def predictNext(self, values):
        value = values[-2][-1]
        for vals in reversed(values[:-2]):
            value = vals[-1] + value
        return value

    def predictPrevious(self, values):
        value = values[-2][0]
        for vals in reversed(values[:-2]):
            value = vals[0] - value
        return value

    def solvePartOne(self, data):
        return sum([self.predictNext(self.extrapolate([[int(x) for x in line.split(' ')]])) for line in data])                    

    def solvePartTwo(self, data):
        return sum([self.predictPrevious(self.extrapolate([[int(x) for x in line.split(' ')]])) for line in data])     
