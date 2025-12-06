from src.PythonFramework.Day import Day
import src.PythonFramework.Algorithms as algs
import re
from math import prod


class Solver(Day):
    test_answers = [4277556, 3263827]
    answers = [6635273135233, 12542543681221]
    operation = {'*': prod, '+': sum}

    def solvePartOne(self, data):
        data = [re.sub('[\ ]+', ' ', string).split() for string in data]
        data = [[int(x) if x not in ['*', '+'] else x for x in line] for line in data]
        data = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
        return sum([self.operation[col[-1]](col[:-1]) for col in data])

    def solvePartTwo(self, data):
        # Transpose data to look at columns
        data = [[data[j][i] for j in range(len(data))] for i in reversed(range(len(data[0])))]
        data = [''.join(l).replace(' ', '') for l in data]
        # Separate operators
        data = [re.sub('[+*]','',data[i]) if data[i] != '' else data[i-1][-1] for i in range(len(data))] + [data[-1][-1]]
        result, numbers = 0, []
        for string in data:
            if string in ['+', '*']:
                result += self.operation[string](numbers)
                numbers = []
                continue
            numbers.append(int(string))
        return result
