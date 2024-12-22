import sys
sys.path.append('../../src')

from PythonFramework.Day import Day


def numberIsPart(x, y, length, data):
    max_x = len(data[0])
    max_y = len(data)
    for i in range(x-1, x+length+1):
        for j in range(y-1, y+2):
            if i >= 0 and i < max_x and j >= 0 and j < max_y:
                char = data[j][i]
                if char != '.' and not char.isnumeric():
                    return True
    return False


def getNumberLength(x, y, data):
    max_x = len(data[y])
    length = 0
    while x < max_x and data[y][x].isnumeric():
        x += 1
        length += 1
    return length


def getNumberStart(x, y, data):
    while data[y][x-1].isnumeric():
        x -= 1
    return x


def gearNumbers(x, y, data):
    numbers = []
    for j in range(y-1, y+2):
        i = x-1
        while i < x+2:
            if data[j][i].isnumeric():
                start = getNumberStart(i, j, data)
                length = getNumberLength(start, j, data)
                i += start - i + length
                numbers.append(int(data[j][start:start+length]))
            else:
                i += 1
    return numbers


class Day3(Day):
    def solvePartOne(self, data):
        parts = []
        max_x = len(data[0])
        for y, line in enumerate(data):
            x = 0
            while x < max_x:
                char = line[x]
                if char.isnumeric():
                    length = getNumberLength(x, y, data)
                    if numberIsPart(x, y, length, data):
                        # print(f'x: {x}, y: {y}, num: {line[x:x+length]}, len: {length}, part!')
                        parts.append(int(line[x:x+length]))
                    # else:
                        # print(f'x: {x}, y: {y}, num: {line[x:x+length]}, len: {length}, NO PART!')
                    x += length
                else:
                    x += 1
        return sum(parts)

    def solvePartTwo(self, data):
        gears = []
        for y, line in enumerate(data):
            for x, char in enumerate(line):
                if char == '*':
                    numbers = gearNumbers(x, y, data)
                    if len(numbers) == 2:
                        gears.append(numbers[0] * numbers[1])
        return sum(gears)

Day3(3).getResult()
