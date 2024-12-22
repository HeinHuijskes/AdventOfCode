import sys
sys.path.append('../../src')

from PythonFramework.Day import Day


class Day2(Day):
    def executeProgram(self, noun, verb, program):
        program[1] = noun
        program[2] = verb
        for i in range(0, len(program), 4):
            if program[i] == 99:
                return program[0]
            if program[i] == 1:
                program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
            else:
                program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]

    def solvePartOne(self, data):
        program = [int(x) for x in data[0].split(',')[:-1]]
        return self.executeProgram(12, 2, program)

    def solvePartTwo(self, data):
        program = [int(x) for x in data[0].split(',')[:-1]]
        for i in range(0, 100):
            for j in range(0, 100):
                if self.executeProgram(i, j, program.copy()) == 19690720:
                    return 100 * i + j


Day2(2).getResult()
