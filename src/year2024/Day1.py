import sys
sys.path.append('../../src')

from PythonFramework.Day import Day


class Day1(Day):
    def solvePartOne(self, data):
        first, second = [], []
        for line in data:
            numbers = line.split('   ')
            first.append(int(numbers[0]))
            second.append(int(numbers[1]))
        first = list(sorted(first))
        second = list(sorted(second))
        return sum([abs(first[i]-second[i]) for i in range(len(first))])

    def solvePartTwo(self, data):
        first, second = [], []
        for line in data:
            numbers = line.split('   ')
            first.append(int(numbers[0]))
            second.append(int(numbers[1]))
        checked = {}
        result = 0
        for number in first:
            if number in checked.keys():
                result += number*checked[number]
            else:
                amount = 0
                for nr in second:
                    if nr == number:
                        amount += 1
                result += number*amount
                checked[number] = amount
        return result


Day1(1).getResult()
