import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day
from functools import reduce


class Day3(Day):
    def solvePartOne(self, data):
        # In essence how most of my one-liners work is by going over a set data in small steps, 
        # where each step some computation provides a slightly modified set of data that is piped into to the next step.
        # E.g. at some point below some duplicates are found, so that data is piped through the set() function, so that in the next step all duplicates are removed

        # For the correct order of operations, read from the bottom upwards (except read the discription above each indented part first)
        # This oneliner very likely can still be heavily optimized/shortened

        # Take the positions of all given numbers and sum them
        return sum(
            # Find the lengths of numbers by looking ahead 2 spaces and seeing if those spaces are numbers
            [int(data[y][x:x+1+data[y][x+1].isnumeric()+data[y][x:x+3].isnumeric()])
            for x, y in
            # Flatten the list of lists of tuples to just a long list of tuples, and compute the set to get rid of duplicate coordinates
            set(list(reduce(lambda a, b: a + b, 
            # Compute all coordinates of all numbers directly surrounding part-symbols
                [
                    # Compute all numbers around each part-symbol
                    [
                        # Offset i (the number's x-coord) by the amount of numbers preceeding it, to get to the start of the number (numbers have max length 3)
                        (i-
                            data[j][i-1].isnumeric()-data[j][i-2:i].isnumeric()
                        , j)
                        # Loop over all characters in a radius of 1 from the part-symbol, including diagonals
                        for i in range(x-1, x+2) for j in range(y-1, y+2)
                        # Only add a character's coords to the resulting list if it is numeric
                        if data[j][i].isnumeric()
                    ]
                # Compute the coordinates of part-symbols
                for x in range(len(data[0])) for y in range(len(data))
                    # All non-numeric and non-dot symbols are part symbols 
                    if not data[y][x].isnumeric() and not data[y][x] == '.'
                ]
            ,[])))
            ])

    def solvePartTwo(self, data):
        # Loop over all found sets of 2 numbers, where each set contains the two numbers surrounding a certain gear
        return sum([a*b for [a, b] in 
            # Find the lengths of numbers by looking ahead 2 spaces and seeing if those spaces are numbers
            # Python can add boolean values to integers!
            [[int(data[y][x:x+
                # x cannot go out of bounds here, since all gears in the given dataset are at least 1 space away from the edge
                (data[y][x+1].isnumeric())+
                (data[y][x:x+3].isnumeric())+1
                ]) for (x, y) in gearList] for gearList in 
            # Compute all non-duplicate coordinates of all gears having exactly 2 surrounding numbers
            [e for e in [
                # Compute the set to remove duplicates
                set([
                    # Offset i (the number's x-coord) by the amount of numbers preceeding it, to get to the start of the number (numbers have max length 3)
                    (i-
                        # Same boolean trick as above, now with subtraction
                        data[j][i-1].isnumeric()-data[j][i-2:i].isnumeric()
                    , j)
                    # Loop over all characters in a radius of 1 from the gear-symbol, including diagonals
                    for i in range(x-1, x+2) for j in range(y-1, y+2)
                    # Only add a character's coords to the resulting list if it is numeric
                    if data[j][i].isnumeric()
                ])
                # Compute the coordinates of gear-symbols
                for x in range(len(data[0])) for y in range(len(data))
                    # Only include gear-symbols
                    if data[y][x] == '*']
            # Exclude gears that do not have exactly 2 numbers neighbouring them
            if len(e) == 2]]])


Day3().getResult()
