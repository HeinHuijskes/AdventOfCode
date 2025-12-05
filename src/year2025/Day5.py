from src.PythonFramework.Day import Day
import src.PythonFramework.Algorithms as algs


class Solver(Day):
    test_answers = [3, 14]
    answers = [758, 343143696885053]

    def parse(self, data: list[str]):
        split = data.index('')
        ranges = [[int(x) for x in r.split('-')] for r in data[:split]]
        ids = [int(id) for id in data[split+1:]]
        return ranges, ids

    def solvePartOne(self, data):
        ranges, ids = data
        result = 0
        for id in ids:
            for first, second in ranges:
                if first <= id <= second:
                    result += 1
                    break
        return result

    def solvePartTwo(self, data):
        ranges, _ = data
        change = True
        while change:
            change = False
            result = []

            while len(ranges) > 0:
                new_range = ranges.pop()

                for index_y, (first_y, second_y) in enumerate(ranges):
                    first_x, second_x = new_range

                    if (first_x <= second_y) and (first_y <= second_x):
                        new_range = (min(first_x, first_y), max(second_x, second_y))
                        ranges.pop(index_y)
                        change = True

                result.append(new_range)
            ranges = result

        return sum([s-f+1 for f,s in ranges])
