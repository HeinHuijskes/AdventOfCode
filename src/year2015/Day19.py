from src.PythonFramework.Day import Day


class Solver(Day):
    def parse(self, data):
        medicine = data[-1]
        replacements = [line.split(' => ') for line in data[:-2]]
        return medicine, replacements

    def sortByLength(self, array):
        length = max([len(b) for a, b in array])
        result = []
        while len(result) < len(array):
            for a, b in array:
                if len(b) == length:
                    result.append((a, b))
            length -= 1
        return result

    def solvePartOne(self, data):
        start, replacements = data
        results = set()
        for initial, replacement in replacements:
            for i, molecule in enumerate(start):
                if i+1 < len(start) and start[i+1].islower():
                    molecule = molecule + start[i+1]
                if initial == molecule:
                    results.add(start[:i] + replacement + start[i+len(initial):])
        return len(results)

    def solvePartTwo(self, data):
        goal, replacements = data
        replacements = self.sortByLength(replacements)
        queue = [(0, goal)]
        string = goal
        # Work backwards, starting at the goal and replacing molecules until only 'e' is left
        while string != 'e':
            # Depth first, hope that the answer is correct with the greedy approach
            steps, string = queue.pop()
            length = None
            for replacement, initial in replacements:
                if initial not in string:
                    continue
                if length == None:
                    length = len(initial)
                if len(initial) < length:
                    # Greedy approach: assume one of the longest possible reductions is always correct
                    break
                index = string.index(initial)
                newArray = string[:index] + replacement + string[index+len(initial):]
                newEntry = (steps+1, newArray)
                if newEntry not in queue:
                    queue.append((steps+1, newArray))
        return steps
