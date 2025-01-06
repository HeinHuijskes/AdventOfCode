import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Solver(Day):
    def parse(self, data):
        program = []
        for line in data:
            line = line.split(', ')
            if len(line) == 1:
                instruction, rest = line[0].split(' ')
                if instruction == 'jmp':
                    rest = int(rest)
                program.append([instruction, rest])
            else:
                program.append(line[0].split(' ') + [int(line[1])])
        return program

    def solve(self, data, registers):
        i = 0
        while 0 <= i < len(data):
            line = data[i]
            instruction, value = line[0], line[1]
            if instruction == 'hlf':
                registers[value] //= 2
            elif instruction == 'tpl':
                registers[value] *= 3
            elif instruction == 'inc':
                registers[value] += 1
            elif instruction == 'jmp':
                i += value - 1
            elif instruction == 'jie':
                if registers[value] % 2 == 0:
                    i += line[2] - 1
            elif instruction == 'jio':
                if registers[value] == 1:
                    i += line[2] - 1
            i += 1
        return registers['b']

    def solvePartOne(self, data):
        return self.solve(data, {'a': 0, 'b': 0})

    def solvePartTwo(self, data):
        return self.solve(data, {'a': 1, 'b': 0})


Solver(day=23).getResult(testOnly=False)
