import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Day23(Day):
    def parse(self, data):
        connections = {}
        for line in data:
            cpu1, cpu2 = line.split('-')
            if cpu1 not in connections:
                connections[cpu1] = []
            if cpu2 not in connections:
                connections[cpu2] = []
            connections[cpu1].append(cpu2)
            connections[cpu2].append(cpu1)
        return connections

    def solvePartOne(self, data):
        connections = data
        threeways = set()
        for cpu1 in connections:
            cpus = connections[cpu1]
            for i, cpu2 in enumerate(cpus[:-1]):
                for cpu3 in cpus[i+1:]:
                    if cpu3 in connections[cpu2]:
                        threeway = tuple(sorted([cpu1, cpu2, cpu3]))
                        threeways.add(threeway)
        tthreeways = [t for t in threeways if t[0].startswith('t') or t[1].startswith('t') or t[2].startswith('t')]
        return len(tthreeways)

    def solvePartTwo(self, data):
        connections = data
        cpu_pairs = [tuple([connection]) for connection in connections.keys()]
        # Take each possible pair of 2 way connections first. Then expand to 3, then 4, etc.
        # Quit when only one pair of unknown max length is left, that is the result.
        while len(cpu_pairs) > 1:
            new_cpu_pairs = set()
            for pair in cpu_pairs:
                for new_cpu in connections:
                    if new_cpu in pair:
                        continue
                    fully_connected = True
                    new_cpu_connections = connections[new_cpu]
                    for cpu in pair:
                        if cpu not in new_cpu_connections:
                            fully_connected = False
                            break
                    if fully_connected:
                        new_pair = tuple(sorted(list(pair) + [new_cpu]))
                        new_cpu_pairs.add(new_pair)
            cpu_pairs = new_cpu_pairs
            print(f'Round {len(list(cpu_pairs)[0])}: {len(cpu_pairs)}')
        password = ','.join(cpu_pairs.pop())
        return password

Day23(23).getResult(testOnly=False)
