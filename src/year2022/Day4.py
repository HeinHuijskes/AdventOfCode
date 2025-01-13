from src.PythonFramework.Day import Day

import re as regex


class Solver(Day):
    def solvePartOne(self, data):
        result = []
        for chunk in data:
            # Parse the data, where 'a-b,x-y' represents a chunk of data
            [a, b, x, y] = regex.split(',|-', chunk)
            # Convert to integers
            [a, b, x, y] = list(map(int, [a, b, x, y]))
            # Check if either range lies within the other
            is_inside = (a <= x and b >= y) or (a >= x and b <= y)
            result.append(is_inside)
        # Sum up all the truth values for the final score
        return sum(result)

    def solvePartTwo(self, data):
        result = []
        for chunk in data:
            # Same as part 1
            [a, b, x, y] = regex.split(',|-', chunk)
            [a, b, x, y] = list(map(int, [a, b, x, y]))
            # The only cases without overlap are when b < x or when a > y
            has_overlap = not (b < x or a > y)
            result.append(has_overlap)
        return sum(result)
