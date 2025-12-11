from src.PythonFramework.Day import Day
from itertools import combinations
import numpy as np
import z3

class Solver(Day):
    test_answers = [7, 33]
    answers = [404, 16474]

    def parse(self, data: list[str]):
        goals, button_list, joltages = [], [], []
        for line in data:
            split = line.split()
            goals.append([x == '#' for x in split[0][1:-1]])
            button_list.append([tuple(int(x) for x in button[1:-1].split(',')) for button in split[1:-1]])
            joltages.append([int(x) for x in split[-1][1:-1].split(',')])
        return goals, button_list, joltages

    def findShortestButtonCombo(self, goal, buttons):
        for j in range(1, len(buttons)+1):
            combs = list(combinations(buttons, j))
            for comb in combs:
                state = [False for k in range(len(goal))]
                for button in comb:
                    state = [state[l] ^ (l in button) for l in range(len(state))]
                if state == goal:
                    return len(comb)
        return 0

    def solvePartOne(self, data):
        goals, buttonslist, _ = data
        total = 0
        for i in range(len(goals)):
            goal, buttons = goals[i], buttonslist[i]
            result = self.findShortestButtonCombo(goal, buttons)
            total += result
        return total

    def solvePartTwo(self, data):
        _, buttonslist, joltages = data
        total = 0

        for i in range(len(joltages)):
            joltage, buttons = joltages[i], buttonslist[i]
            s = z3.Optimize()

            integers = [z3.Int(f'x{i}') for i in range(len(buttons))]
            for x in integers:
                s.add(x >= 0)

            for i, jolt in enumerate(joltage):
                summation = [integers[j] for j in range(len(buttons)) if i in buttons[j]]
                s.add(sum(summation) == jolt)

            s.minimize(sum(integers))
            s.check()
            model = s.model()

            result = sum([model[x].as_long() for x in integers])
            total += result
        return total
