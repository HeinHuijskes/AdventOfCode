import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Day17(Day):
    goal = 150
    def parse(self, data):
        containers = list(sorted([int(line) for line in data]))
        return containers

    def solvePartOne(self, data):
        # This implementation is very slow
        result = [[]]
        queue = [(data[i], [i]) for i in range(len(data))]
        round = 0
        round_amount = 0
        new_queue = []
        while len(queue) > 0:
            total, containers = queue.pop(0)
            if len(containers) > round:
                round = len(containers)
                print(f'Round: {round}')
                print(f'Checked: {round_amount}')
                round_amount = 0
                result.append([])
            else:
                round_amount += 1
            if total == self.goal:
                result[round].append(containers)
            else:
                for i in range(len(data)):
                    amount = total + data[i]
                    if amount > self.goal or i in containers:
                        continue
                    new_containers = list(sorted(containers + [i]))
                    new_tuple = (amount, new_containers)
                    if new_containers not in result[round] and new_tuple not in new_queue:
                        new_queue.append(new_tuple)
            if len(queue) == 0 and len(new_queue) > 0:
                queue = new_queue
                new_queue = []
        return sum([len(r) for r in result])

    def solvePartTwo(self, data):
        result = [[]]
        queue = [(data[i], [i]) for i in range(len(data))]
        round = 0
        round_amount = 0
        new_queue = []
        found_solution = False
        while len(queue) > 0:
            total, containers = queue.pop(0)
            if len(containers) > round:
                if found_solution:
                    break
                round = len(containers)
                round_amount = 0
                result.append([])
            else:
                round_amount += 1
            if total == self.goal:
                found_solution = True
                result[round].append(containers)
            else:
                for i in range(len(data)):
                    amount = total + data[i]
                    if amount > self.goal or i in containers:
                        continue
                    new_containers = list(sorted(containers + [i]))
                    new_tuple = (amount, new_containers)
                    if new_containers not in result[round] and new_tuple not in new_queue:
                        new_queue.append(new_tuple)
            if len(queue) == 0 and len(new_queue) > 0:
                queue = new_queue
                new_queue = []
        return len(result[round])


Day17(17).getResult(testOnly=False)
