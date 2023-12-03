import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day
from functools import reduce


class Day3(Day):
    def solvePartOne(self, data):
        return sum([int(data[y][x:x+1+data[y][x+1].isnumeric()+data[y][x:x+3].isnumeric()]) for x, y in set(list(reduce(lambda a, b: a + b, [[(i-data[j][i-1].isnumeric()-data[j][i-2:i].isnumeric(), j) for i in range(x-1, x+2) for j in range(y-1, y+2) if data[j][i].isnumeric()] for x in range(len(data[0])) for y in range(len(data)) if not data[y][x].isnumeric() and not data[y][x] == '.'],[])))])

    def solvePartTwo(self, data):
        return sum([a*b for [a, b] in [[int(data[y][x:x+(data[y][x+1].isnumeric())+(data[y][x:x+3].isnumeric())+1]) for (x, y) in gearList] for gearList in [e for e in [set([(i-data[j][i-1].isnumeric()-data[j][i-2:i].isnumeric(), j)  for i in range(x-1, x+2) for j in range(y-1, y+2) if data[j][i].isnumeric()]) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == '*'] if len(e) == 2]]])


Day3().getResult()
