import sys
sys.path.append('../../../src')

import regex as re

from PythonFramework.Day import Day


class Day6(Day):
    def solvePartOne(self, data):
        times = [int(x) for x in data[0].split(':')[1].split(' ') if x != '']
        distances = [int(x) for x in data[1].split(':')[1].split(' ') if x != '']
        options = []
        for i in range(len(times)):
            distance = distances[i]
            time = times[i]
            count = 0
            for j in range(0, time+1):
                if j*(time-j) > distance:
                    count += 1
            options.append(count)

        result = 1
        for res in options:
            result *= res
        return result

    def solvePartTwo(self, data):
        time = int(''.join(re.findall('\d', data[0])))
        distance = int(''.join(re.findall('\d', data[1])))
        left = 0
        right = 0
        for i in range(0, time):
            if i*(time-i) > distance:
                left = i
                break
        for i in reversed(range(0, time)):
            if i*(time-i) > distance:
                right = i
                break
        return right-left+1


Day6().getResult(testOnly=False)
