from src.PythonFramework.Day import Day


class Solver(Day):
    def solvePartOne(self, data):
        return sum([1 if x == '(' else -1 for x in data[0]])

    def solvePartTwo(self, data):
        moves = [1 if x == '(' else -1 for x in data[0]]
        result = 0
        for i, move in enumerate(moves):
            result += move
            if result < 0:
                break
        return i + 1
