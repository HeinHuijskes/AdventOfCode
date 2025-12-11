from src.PythonFramework.Day import Day


class Solver(Day):
    test_answers = [5, 2]
    answers = [472, 526811953334940]

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
    
    def walkThroughTree(self, data, start, goal):
        vars = {start: []}
        values = {start: 1}
        queue = [start]

        # Build a reversed tree in from the starting point outwards
        while len(queue) > 0:
            node = queue.pop(0)
            # Skip end nodes
            if node == 'out':
                continue

            children = data[node]
            for child in children:
                if child not in vars:
                    vars[child] = []
                    # Initially set each node to 0
                    values[child] = 0
                # Add parent node only once
                if node not in vars[child]:
                    vars[child].append(node)
                # Only consider each node once
                if child not in queue:
                    queue.append(child)

        # Now one by one collapse all variables from start to goal
        while len(vars) > 0:
            # Get currently collapsed variables
            collapsed = [node for node in vars if len(vars[node]) == 0]
            if goal in collapsed:
                return values[goal]

            for node in collapsed:
                # Get collapsed value
                vars.pop(node)
                value = values[node]
                for var in vars:
                    parents = vars[var]
                    # Check that this variable didn't sneakily collapse while running the loop
                    # and consider only variables that have the current node as a parent
                    if len(parents) > 0 and node in parents:
                        # Remove the collapsed node from the parents
                        parents.pop(parents.index(node))
                        # And add the parents' value to the current node
                        values[var] += value

    def solvePartTwo(self, data):
        fft = self.walkThroughTree(data, start='svr', goal='fft')
        dac = self.walkThroughTree(data, start='fft', goal='dac')
        out = self.walkThroughTree(data, start='dac', goal='out')
        return fft * dac * out
