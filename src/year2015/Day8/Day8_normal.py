import sys
sys.path.append('../../../src')

import regex as re

from PythonFramework.Day import Day


class Day8(Day):
    def solvePartOne(self, data):
        string_lengths = []
        memory_lengths = []
        for line in data:
            string_length = len(line)
            x_codes = len(re.findall(r"\\x[abcdef\d]{2}", line))
            print(re.findall(r"\\x[abcdef\d]{2}", line))
            quotes = len(re.findall(r"\\\"", line))
            doubles = len(re.findall(r"\\\\", line))
            # print(doubles)
            memory_length = string_length - 3*x_codes - quotes - doubles - 2
            string_lengths.append(string_length)
            memory_lengths.append(memory_length)
            print(string_length, memory_length, line)
        return sum(string_lengths) - sum(memory_lengths)

    def solvePartTwo(self, data):
        return 'No part 2 solution yet'


Day8().getResult(testOnly=True)
