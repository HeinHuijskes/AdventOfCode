from src.PythonFramework.Day import Day


class Solver(Day):
    answers = ['wkbvmikb', 'evakwaga']
    def parse(self, data):
        return [[data[i][j] for i in range(len(data))] for j in range(len(data[0]))]
    
    def solve(self, data, part2=False):
        result = ''
        for col in data:
            mapping = {}
            for letter in col:
                if letter not in mapping:
                    mapping[letter] = 0
                mapping[letter] += 1
            highest = letter
            for letter in mapping:
                if (not part2 and mapping[letter] > mapping[highest]) \
                    or (part2 and mapping[letter] < mapping[highest]):
                    highest = letter
            result += highest
        return result

    def solvePartOne(self, data):
        return self.solve(data)

    def solvePartTwo(self, data):
        return self.solve(data, part2=True)
