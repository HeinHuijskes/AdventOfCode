import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day
from PythonFramework.Algorithms import *


class Day5(Day):
    def parse(self, data):
        rules = {}
        updates = []
        for i, line in enumerate(data):
            if len(line) == 0:
                updates = [list(map(int, l.split(','))) for l in data[i+1:]]
                break
            else:
                key, value = map(int, line.split('|'))
                if key in rules:
                    rules[key].append(value)
                else:
                    rules[key] = [value]
        return rules, updates
    
    def isCorrect(self, update, rules):
        correct = True
        # Run through the update in reverse
        for i, x in enumerate(reversed(update[1:])):
            if not x in rules:
                continue
            ruleset = rules[x]
            # Run through the rest of the update to compare against the current value
            for j, y in enumerate(list(reversed(update))[i+1:]):
                # If 'y' is in the ruleset, it is a violation!
                if y in ruleset:
                    correct = False
                    break
            if not correct:
                break
        return correct
    
    def swap(self, update, i, j):
        return update[:j] + [update[i]] + update[j+1:i] + [update[j]] + update[i+1:]
    
    def fixUpdate(self, update, rules):
        # Naive approach: swap updates every time they are wrong
        # Turns out is wasn't naive at all, it just works
        while True:
            correct = True
            for i, x in enumerate(reversed(update[1:])):
                if not x in rules:
                    continue
                ruleset = rules[x]
                for j, y in enumerate(list(reversed(update))[i+1:]):
                    if y in ruleset:
                        correct = False
                        update = self.swap(update, len(update)-(i+1), len(update)-(j+i+2))
                        break
                if not correct:
                    break
            if correct:
                # Solved!
                break
        return update

    def solvePartOne(self, data):
        rules, updates = data
        results = 0
        for update in updates:
            if self.isCorrect(update, rules):
                results += update[(len(update)-1)//2]

        return results

    def solvePartTwo(self, data):
        rules, updates = data
        results = []
        for update in updates:
            if not self.isCorrect(update, rules):
                fixed_update = self.fixUpdate(update, rules)
                results.append(fixed_update[(len(fixed_update)-1)//2])
        return sum(results)


Day5(5).getResult(testOnly=False)
