import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day


class Day2(Day):
    def solvePartOne(self, data):
        red, green, blue = 12, 13, 14
        total = 0
        for line in data:
            possible = True
            gameid, line = line.split(':')
            gameid = int(gameid[5:])
            sets = line.split(';')
            for gameset in sets:
                colours = gameset.split(',')
                for colour in colours:
                    split = colour.split(' ')
                    number = int(split[1])
                    colour = split[2]
                    if colour == 'red':
                        if number > red:
                            possible = False
                    elif colour == 'green':
                        if number > green:
                            possible = False
                    else:
                        if number > blue:
                            possible = False
            if possible:
                total += gameid
        return total

    def solvePartTwo(self, data):
        total = 0
        for line in data:
            red, green, blue = 0, 0, 0
            sets = line.split(':')[1].split(';')
            # print(sets)
            for gameset in sets:
                colours = gameset.split(',')
                for colour in colours:
                    split = colour.split(' ')
                    number = int(split[1])
                    colour = split[2]
                    if colour == 'red' and number > red:
                        red = number
                    elif colour == 'green' and number > green:
                        green = number
                    elif colour == 'blue' and number > blue:
                        blue = number
            total += red * green * blue
        return total


Day2().getResult()
