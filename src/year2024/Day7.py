import sys
sys.path.append('../../src')

from math import log10

from PythonFramework.Day import Day
from PythonFramework.Algorithms import *


class Day7(Day):
    def parse(self, data):
        test_values = []
        operators = []
        for line in data:
            tv, ops = line.split(': ')
            tv, ops = int(tv), list(map(int, ops.split(' ')))
            test_values.append(tv)
            operators.append(ops)
        return test_values, operators

    def solvePartOne(self, data):
        test_values, operators_list = data
        result = 0
        for i in range(len(test_values)):
            test_value, operators = test_values[i], operators_list[i]
            options = [operators[0]]
            for operator in operators[1:]:
                new_options = []
                for option in options:
                    if option > test_value:
                        continue
                    new_options.append(option * operator)
                    new_options.append(option + operator)
                options = new_options
            if test_value in options:
                result += test_value
        return result

    def solvePartTwo(self, data):
        test_values, operators_list = data
        result = 0
        for i in range(len(test_values)):
            test_value, operators = test_values[i], operators_list[i]
            options = [operators[0]]
            for operator in operators[1:]:
                new_options = []
                for option in options:
                    if option > test_value:
                        continue
                    new_options.append(option * operator)
                    new_options.append(option + operator)
                    new_options.append(10**int(log10(operator)+1)*option+operator)
                options = new_options
            if test_value in options:
                result += test_value
        return result


Day7(7).getResult(testOnly=False)
