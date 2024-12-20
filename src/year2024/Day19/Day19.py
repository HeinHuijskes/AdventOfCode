import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day
from PythonFramework.Algorithms import *


class Day19(Day):
    def parse(self, data):
        return data[0].split(', '), data[2:]
    
    def isValid(self, design, patterns):
        options = ['']
        optimized_patterns = [pattern for pattern in patterns if pattern in design]
        while len(options) > 0:
            new_options = []
            for option in options:
                for pattern in optimized_patterns:
                    if not design[len(option):len(option)+len(pattern)] == pattern:
                        continue
                    new_pattern = option + pattern
                    if len(new_pattern) == len(design):
                        return True
                    new_options.append(option + pattern)
            options = list(set(new_options))
        return False

    def isMoreValid(self, design, patterns):
        options = {'': 1}
        result = 0
        optimized_patterns = [pattern for pattern in patterns if pattern in design]
        while len(options) > 0:
            new_options = {}
            for option in options:
                for pattern in optimized_patterns:
                    if not design[len(option):len(option)+len(pattern)] == pattern:
                        continue
                    new_pattern = option + pattern
                    if len(new_pattern) == len(design):
                        result += options[option]
                        continue
                    if not new_pattern in new_options:
                        new_options[new_pattern] = 0
                    new_options[new_pattern] += options[option]
            options = new_options
        return result
            

    def solvePartOne(self, data):
        patterns, designs = data
        result = 0
        for design in designs:
            result += self.isValid(design, patterns)
        return result

    def solvePartTwo(self, data):
        patterns, designs = data
        result = 0
        for design in designs:
            result += self.isMoreValid(design, patterns)
        return result


Day19().getResult(testOnly=False)
