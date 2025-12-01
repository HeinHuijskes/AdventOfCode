from src.PythonFramework.Day import Day
import src.PythonFramework.Algorithms as algs
from regex import regex


class Solver(Day):
    # testOnly = True
    test_answers = [18, None]
    answers = [102239, None]

    def parse(self, data: list[str]):
        return data

    def solvePartOne(self, data):
        total = []
        line: str = data[0].strip(' ')

        result = ''
        pointer = 0
        while pointer < len(line):
            
            char = line[pointer]
            if char != '(':
                result += char
                pointer += 1
                continue
            
            second_pointer = pointer
            while char != ')':
                second_pointer += 1
                char = line[second_pointer]
            second_pointer += 1
            
            length, amount = [int(num) for num in regex.match('\((\d+)x(\d+)\)', line[pointer:second_pointer]).groups()]
            bit = line[second_pointer:second_pointer+length]
            result += ''.join([bit for i in range(amount)])
            pointer = second_pointer + length

        return len(result)

    def solvePartTwo(self, data):
        return 'No part 2 solution yet'
