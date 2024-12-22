import sys
sys.path.append('../../src')

from PythonFramework.Day import Day


class Day2(Day):
    def checkSafety(self, numbers):
        safe = True
        ascending = numbers[1] > numbers[0]
        nr = numbers[0]
        for number in numbers[1:]:
            if nr == number or (nr > number and ascending) or (nr < number and not ascending) or abs(number - nr) > 3:
                safe = False
                break
            nr = number
        return safe

    def solvePartOne(self, data):
        safe_reports = 0
        for line in data:
            numbers = [int(x) for x in line.split(' ')]
            safe_reports += self.checkSafety(numbers)
        return safe_reports

    def solvePartTwo(self, data):
        safe_reports = 0
        for line in data:
            numbers = [int(x) for x in line.split(' ')]
            safe = self.checkSafety(numbers)
            if not safe:
                for i in range(len(numbers)):
                    nrs = numbers.copy()
                    del nrs[i]
                    safe = self.checkSafety(nrs)
                    if safe:
                        break
            safe_reports += safe
        return safe_reports


Day2(2).getResult()
