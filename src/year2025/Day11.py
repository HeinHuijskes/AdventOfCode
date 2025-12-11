from src.PythonFramework.Day import Day
import src.PythonFramework.Algorithms as algs


class Solver(Day):
    test_answers = [5, 2]
    answers = [472, None]

    def parse(self, data: list[str]):
        connections = {}
        for line in data:
            start, end = line.split(': ')
            connections[start] = end.split()
        return connections

    def solvePartOne(self, data):
        queue = [['you']]
        results = []
        while len(queue) > 0:
            path = queue.pop()
            if path[-1] == 'out':
                results.append(path)
            else:
                nodes = data[path[-1]]
                for node in nodes:
                    queue.append(path+[node])
        return len(results)

    def solvePartTwo(self, data):
        r_data = {}
        for key in data:
            values = data[key]
            for value in values:
                if value not in r_data:
                    r_data[value] = []
                r_data[value].append(key)

        goal = 'svr'
        queue = [['fft']]
        fft_results = []
        while len(queue) > 0:
            path = queue.pop()
            if path[-1] == goal:
                fft_results.append(path)
            else:
                nodes = r_data[path[-1]]
                for node in nodes:
                    queue.append(path+[node])

        lengths = {}
        for result in fft_results:
            if len(result) not in lengths:
                lengths[len(result)] = 0
            lengths[len(result)] += 1

        goal = 'out'
        queue = [['dac']]
        dac_results = []
        while len(queue) > 0:
            path = queue.pop()
            if path[-1] == goal:
                dac_results.append(path)
            else:
                nodes = data[path[-1]]
                for node in nodes:
                    queue.append(path+[node])

        lengths = {}
        for result in dac_results:
            if len(result) not in lengths:
                lengths[len(result)] = 0
            lengths[len(result)] += 1

        dacs_blacklist = []
        for result in dac_results:
            for node in result:
                if node != 'dac' and node not in dacs_blacklist:
                    dacs_blacklist.append(node)

        m_data = {}
        for key in data:
            value = data[key]
            if key not in dacs_blacklist:
                m_data[key] = value
            else:
                m_data[key] = []

        goal = 'dac'
        queue = [['fft']]
        results = []
        while len(queue) > 0:
            path = queue.pop()
            if path[-1] == goal:
                results.append(path)
            else:
                nodes = m_data[path[-1]]
                for node in nodes:
                    queue.append(path+[node])

        lengths = {}
        for result in results:
            if len(result) not in lengths:
                lengths[len(result)] = 0
            lengths[len(result)] += 1

        return len(fft_results) * len(dac_results) * len(results)
