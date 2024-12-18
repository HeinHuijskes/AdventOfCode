import sys
sys.path.append('../../../src')

from functools import reduce

from PythonFramework.Day import Day


class Day2(Day):
    def solvePartOne(self, data):
        # Return the sum of all game ids
        return sum([
            # Take the gameid from each correct game
            d[0] for d in [
                # Flatten all inner lists
                list(reduce(lambda a, b: a + b, [
                    [
                        # Return a game id
                        i+1 
                        # Check that a value is not over the limit
                        if \
                            # Dict to look up the allowed values
                            {'red': 12, 'green': 13, 'blue': 14}[
                                # The given colour that needs to be checked
                                a.split(' ')[2]
                            ]
                            # Check that the amount is not too high
                            >= int(a.split(' ')[1]) 
                        # Return 0 as an indicator of an impossible game
                        else 0 
                        # Loop over all picks within a gameset
                        for a in b.split(',')]
                    # Loop over all sets within a game
                    for b in l.split(':')[1].split(';')
                ], []))
                # Loop over all lines in the data
                for i, l in enumerate(data)
            ]
            # Discard games that contain impossible values
            if 0 not in d
        ])

    def solvePartTwo(self, data):
        # Return the sum of the powers of the sets of cubes
        return sum([a*b*c for a,b,c in 
            # Zip the found values to group the gameids back together
            list(zip(*
                [
                    [
                        # Only consider the largest value of this colour in this game
                        max(w) if len(w) > 0 else 0 for w in 
                        [
                            [
                                # Look at the numbers of a colour, which are located at indexes with intervals of 2
                                # Group these numbers by colour, by comparing the interval + 1 to colour c
                                int(v) for i, v in enumerate(x) if i % 2 == 0 and x[i+1] == c
                            ]
                        # Extra loop to be able to access game arrays by index, as well as object (e.g. to enable x[i+1] as used above)
                        for x in 
                            [
                                # Parse all numbers and colours into one array per game
                                ''.join(''.join(l.split(':')[1].split(';')).split(',')).split(' ')[1:]
                                for l in data
                            ]
                        ]
                    ]
                # Separate the numbers per game based on colour
                for c in ['red', 'green', 'blue']
                ]
            ))
        ])


Day2().getResult()
