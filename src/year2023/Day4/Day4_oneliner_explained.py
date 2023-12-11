import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day


class Day4(Day):
    def solvePartOne(self, data):
        # Calculate the points based on the amount of winning numbers on each card
        return sum([2**(b-1) for b in 
            [
                # The intersection of winning numbers and card numbers contains the winning card numbers
                len(a.intersection(b)) for a, b in 
                    [
                        [
                            # Transform the winning numbers and card numbers into sets
                            # This assumes that card numbers and winning numbrs are both unique
                            set([
                                    # Split on space and discard empty spaces 
                                    # (which are a result of single digit numbers having multiple spaces)
                                    a for a in s.split(' ') if a != ''
                                ]) 
                            # Discard the "Card x:" part and split data into winning numbers and card numbers
                            for s in l.split(': ')[1].split(' | ')
                        ]
                        # Loop over all lines
                        for l in data
                    ]
            ]
        # Only consider cards with at least 1 winning number
        if b > 0])

    def solvePartTwo(self, data):
        return 'No implementation yet'


Day4().getResult()
