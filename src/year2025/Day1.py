from src.PythonFramework.Day import Day
import src.PythonFramework.Algorithms as algs


class Solver(Day):
    test_answers = [3, 6]
    answers = [1034, 6166]

    def parse(self, data: list[str]):
        self.dirs = {'R': 1, 'L': -1}
        return [(entry[0], int(entry[1:])) for entry in data]

    def solvePartOne(self, data):
        state, counter = 50, 0
        for dir, amount in data:
            state = (state + self.dirs[dir] * amount) % 100
            counter += state == 0
        return counter

    def solvePartTwo(self, data):
        state, counter = 50, 0

        for dir, amount in data:
            hundreds = amount // 100
            amount -= hundreds * 100

            newstate = (state + self.dirs[dir] * amount)
            newerstate = newstate % 100
            pass_zero = (newerstate == 0) or (newerstate != newstate and state != 0)

            counter += pass_zero + hundreds
            state = newerstate

        return counter
