from src.PythonFramework.Day import Day
import src.PythonFramework.Algorithms as algs
import re
from math import prod


class Solver(Day):
    test_answers = [4277556, 3263827]
    answers = [6635273135233, 12542543681221]

    def parse(self, data: list[str]):
        return data

    def solvePartOne(self, data):
        data = [re.sub('[\ ]+', ' ', string).split() for string in data]
        data = [[int(x) if x not in ['*', '+'] else x for x in line] for line in data]
        data = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
        result = 0
        for col in data:
            numbers = col[:-1]
            operator = col[-1]
            if operator == '+':
                result += sum(numbers)
            else:
                result += prod(numbers)
        return result

    def solvePartTwo(self, data):
        data = [[data[j][i] for j in range(len(data))] for i in reversed(range(len(data[0])))]
        data = [''.join(l).replace(' ', '') for l in data]
        result = 0
        numbers = []
        for string in data:
            operator = ''
            if string == '':
                continue
            if string[-1] in ['+', '*']:
                string, operator = string[:-1], string[-1]
            numbers.append(int(string))
            if operator != '':
                if operator == '+':
                    result += sum(numbers)
                else:
                    result += prod(numbers)
                operator, numbers = '', []
        return result
