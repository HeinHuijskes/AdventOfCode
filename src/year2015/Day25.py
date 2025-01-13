from src.PythonFramework.Day import Day
from regex import regex


class Solver(Day):
    def parse(self, data):
        row, column = regex.match(
            'To continue, please consult the code grid in the manual.  Enter the code at row (\d+), column (\d+).',
                data[0]).groups()
        return int(row), int(column)
    
    def getNumber(self, row, col):
        # Calculate the number by considering a triangle with length "side=row+col-2",
        # and an extra diagonal with "col" amount of numbers in it
        side = row + col - 2
        return int((side+1)*(side/2) + col)

    def solvePartOne(self, data):
        row, col = data
        number, mult, div = 20151125, 252533, 33554393
        for i in range(2, self.getNumber(row, col)+1):
            number = (number * mult) % div
        return number

    def solvePartTwo(self, data):
        return 'No part 2 solution yet'
