import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Day14(Day):
    def parse(self, data):
        speeds = []
        for line in data:
            words = line.split(' ')
            reindeer, speed, time, rest = words[0], int(words[3]), int(words[6]), int(words[13])
            speeds.append((reindeer, speed, time, rest))
        return speeds

    def solvePartOne(self, data):
        results = []
        race_time = 1000
        for reindeer, speed, time, rest in data:
            mod_time = race_time // (time+rest)
            result = mod_time * speed * time + min((race_time-mod_time), time) * speed
            results.append(result)
        return max(results)

    def solvePartTwo(self, data):
        results = [0 for i in range(len(data))]
        distances = [0 for i in range(len(data))]
        for i in range(2503):
            for j, (reindeer, speed, time, rest) in enumerate(data):
                if i % (time + rest) < time:
                    distances[j] += speed
            maximum = max(distances)
            for j in range(len(distances)):
                if distances[j] == maximum:
                    results[j] += 1
        return max(results)


Day14(14).getResult(testOnly=False)
