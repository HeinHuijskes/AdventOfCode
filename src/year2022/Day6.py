from src.PythonFramework.Day import Day


class Solver(Day):
    def parse(self, data):
        return data[0]

    def solvePartOne(self, data):
        for i in range(0, len(data)):
            chars = data[i:i+4]
            if chars[0] not in chars[1:] and chars[1] not in chars[2:] and chars[2] not in chars[3:]:
                return i + 4

    def solvePartTwo(self, data):
        def recursion(chars):
            if len(chars) == 1:
                return True
            elif chars[0] in chars[1:]:
                return False
            else:
                return recursion(chars[1:])

        n = 14
        for i in range(0, len(data)):
            if recursion(data[i:i+n]):
                return i + n
