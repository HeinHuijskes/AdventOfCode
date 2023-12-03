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

        # Take the positions of all given numbers, extract them from the data based on length, turn them into an integer, and sum them
        return sum([int(data[y][x:x+l]) for (x,y,l) in
            # Find the lengths of numbers by looking ahead 2 spaces and seeing if those spaces are numbers
            [(x, y, sum(
                [x+1 < len(data[0]) and data[y][x+1].isnumeric(), 
                 x+2 < len(data[0]) and data[y][x+1].isnumeric() and data[y][x+2].isnumeric()]
                )+1) for (x, y) in
            # Compute the set to get rid of duplicate coordinates
            set(
            # Flatten the list of lists of tuples to just a long list of tuples
            list(reduce(lambda x, y: x + y, 
            # Compute all coordinates of all numbers directly surrounding part-symbols
            [(lambda x, y: ([
                # Offset i (the number's x-coord) by the amount of numbers preceeding it, to get to the start of the number (numbers have max length 3)
                (i-sum([
                    data[j][i-1].isnumeric(), 
                    data[j][i-1].isnumeric() and data[j][i-2].isnumeric()])
                , j)
                # Loop over all characters in a radius of 1 from the part-symbol, including diagonals
                 for i in range(x-1, x+2) for j in range(y-1, y+2)
                 # Only add a character's coords to the resulting list if it is numeric
                 if data[j][i].isnumeric()
            ]))(x, y) 
            # Compute the coordinates of part-symbols
            for x in range(len(data[0])) for y in range(len(data))
                # All non-numeric and non-dot symbols are part symbols 
                if not data[y][x].isnumeric() and not data[y][x] == '.'], \
            [])))]])

    def solvePartTwo(self, data):
        return sum([
                # First number
                int(data[y][x:x+z]) *
                # Second number 
                int(data[b][a:a+c]) 
                # Loop over the lists of 2 number tuples, where each list represents a found gear that has two numbers surrounding it
                for [(x,y,z),(a,b,c)] in 
            # Find the lengths of numbers by looking ahead 2 spaces and seeing if those spaces are numbers
            [[(x, y, sum(
                [x+1 < len(data[0]) and data[y][x+1].isnumeric(), 
                 x+2 < len(data[0]) and data[y][x+1].isnumeric() and data[y][x+2].isnumeric()]
                )+1) for (x, y) in gearList] for gearList in 
            # Discard all gears without exactly 2 neighbours (see line ...)
            [set(entry) for entry in 
            # Compute all coordinates of all numbers directly surrounding gear-symbols
            [(lambda x, y: ([
                # Offset i (the number's x-coord) by the amount of numbers preceeding it, to get to the start of the number (numbers have max length 3)
                (i-sum([
                    data[j][i-1].isnumeric(), 
                    data[j][i-1].isnumeric() and data[j][i-2].isnumeric()])
                , j)
                # Loop over all characters in a radius of 1 from the gear-symbol, including diagonals
                 for i in range(x-1, x+2) for j in range(y-1, y+2)
                 # Only add a character's coords to the resulting list if it is numeric
                 if data[j][i].isnumeric()
            ]))(x, y) 
            # Compute the coordinates of gear-symbols
            for x in range(len(data[0])) for y in range(len(data))
                # Only include gear-symbols
                if data[y][x] == '*']
            # Exclude gears that do not have exactly 2 numbers neighbouring them
            if len(set(entry)) == 2]]])


Day3().getResult()
