from src.PythonFramework.Day import Day

import regex as re
import math


class Solver(Day):
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
        t = int(''.join(re.findall('\d', data[0])))
        d = int(''.join(re.findall('\d', data[1])))
        x_1 = (-t - math.sqrt(t**2-4*d))/-2
        x_2 = (-t + math.sqrt(t**2-4*d))/-2
        return math.ceil(x_1) - math.ceil(x_2)
