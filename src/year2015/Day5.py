import sys
sys.path.append('../../src')

import regex as re

from PythonFramework.Day import Day


class Day5(Day):
    def solvePartOne(self, data):
        counter = 0
        for line in data:
            vowels = sum([x in 'aeoiu' for x in line])
            hasBadString = sum([x in line for x in ['ab', 'cd', 'pq', 'xy']]) > 0
            hasDuplicate = sum([x == line[i+1] for i, x in enumerate(line[:-1])]) > 0
            if vowels >= 3 and not hasBadString and hasDuplicate:
                counter += 1
        return counter

    def solvePartTwo(self, data):
        counter = 0
        for line in data:
            pairs = [line[i:i+2] for i in range(len(line)-1)]
            hasDoublePair = False
            for i, pair in enumerate(pairs):
                for j in range(i+2, len(pairs), 1):
                    if pair == pairs[j]:
                        hasDoublePair = True
                        break
                if hasDoublePair:
                    break
            if not hasDoublePair:
                continue
            for i, l in enumerate(line[:-2]):
                if l == line[i+2]:
                    counter += 1
                    print(line)
                    break
        return counter


Day5(5).getResult()
