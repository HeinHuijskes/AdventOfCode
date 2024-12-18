import sys
sys.path.append('../../../src')

import regex as re

from PythonFramework.Day import Day


class Day1(Day):
    def solvePartOne(self, data):
        return sum([int(''.join(re.findall('[0-9]', line))[0])*10 + int(''.join(re.findall('[0-9]', line))[-1]) for line in data])

    def solvePartTwo(self, data):
        numbers = [re.findall('one|two|three|four|five|six|seven|eight|nine|[1-9]', line, overlapped=True) for line in data]
        nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
        first = [nums[num[0]]*10 if num[0] in nums.keys() else int(num[0])*10 for num in numbers]
        second = [nums[num[-1]] if num[-1] in nums.keys() else int(num[-1]) for num in numbers]
        return sum([first[i] + second[i] for i in range(len(first))])

Day1().getResult()
