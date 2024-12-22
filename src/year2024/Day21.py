import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Day21(Day):
    def dictifyPads(self, numpad, dirpad):
        numpad = {val: (x, y) for y, line in enumerate(numpad) for x, val in enumerate(line) if not (x == 0 and y == 3)}
        dirpad = {val: (x, y) for y, line in enumerate(dirpad) for x, val in enumerate(line) if not (x == 0 and y == 0)}
        return numpad, dirpad

    def parse(self, data):
        codes = [[x for x in line] for line in data]
        numpad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]
        dirpad = [[None, (0, -1), 'A'], [(-1, 0), (0, 1), (1, 0)]]
        numpad, dirpad = self.dictifyPads(numpad, dirpad)
        return codes, numpad, dirpad
    
    def findPadSequence(self, pad, code, old_x, old_y, gap_x, gap_y):
        sequence = []
        for key in code:
            if type(key) == tuple:
                dx, dy = key
                key = (dx//(max(1, abs(dx))), dy//(max(1, abs(dy))))

            new_x, new_y = pad[key]
            if new_x-old_x == 0 or new_y-old_y == 0: # Straight line
                if not (new_x-old_x == 0 and new_y-old_y == 0):
                    sequence.append((new_x-old_x, new_y-old_y))

            elif (new_x > old_x):  # v> or ^>; y direction has priority
                if old_x == gap_x and new_y == gap_y:
                    # Danger of going over a hole, priority is overruled
                    sequence += [(new_x-old_x, 0), (0, new_y-old_y)]
                else:
                    sequence += [(0, new_y-old_y), (new_x-old_x, 0)]

            else:  # <v or <^; x direction has priority
                if new_x == gap_x and old_y == gap_y:
                    # Danger of going over a hole, priority is overruled
                    sequence += [(0, new_y-old_y), (new_x-old_x, 0)]
                else:
                    sequence += [(new_x-old_x, 0), (0, new_y-old_y)]

            if type(key) != tuple:
                sequence.append('A')
            else:
                for i in range(max(abs(dx),abs(dy))):
                    sequence.append('A')

            old_x, old_y = new_x, new_y
        return sequence

    def subSequences(self, sequence, amount, sub_sequences):
        sub_sequence = []
        for char in sequence:
            sub_sequence.append(char)
            if char == 'A':  # End of subsequence
                sub_sequence = tuple(sub_sequence)  # Lists do not work for dicts
                if sub_sequence not in sub_sequences:
                    sub_sequences[sub_sequence] = 0
                sub_sequences[sub_sequence] += amount
                sub_sequence = []
        return sub_sequences

    def solve(self, data, robots=2):
        codes, numpad, dirpad = data
        results = []
        for code in codes:
            sequence = self.findPadSequence(numpad, code, 2, 3, 0, 3)
            sub_sequences = self.subSequences(sequence, 1, {})

            for i in range(robots+1):
                new_sub_sequences = {}
                for sequence in sub_sequences:
                    amount = sub_sequences[sequence]
                    sequence = self.findPadSequence(dirpad, sequence, 2, 0, 0, 0)
                    self.subSequences(sequence, amount, new_sub_sequences)
                sub_sequences = new_sub_sequences

            length = sum(sub_sequences.values())
            number = int(f'{code[0]}{code[1]}{code[2]}')
            results.append(length*number)

        return sum(results)

    def solvePartOne(self, data):
        return self.solve(data)

    def solvePartTwo(self, data):
        return self.solve(data, 25)


Day21(21).getResult(testOnly=False)
