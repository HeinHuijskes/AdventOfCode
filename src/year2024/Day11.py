from src.PythonFramework.Day import Day

from math import log10, ceil


class Day11(Day):
    def parse(self, data):
        return {int(x): 1 for x in data[0].split(' ')}

    def addStone(self, stone_map, stone, original):
        if stone not in stone_map:
            stone_map[stone] = original
        else:
            stone_map[stone] += original
        return

    def multiplyStones(self, stone_map, length):
        for i in range(length):
            stones = {1: 0}

            for stone in stone_map:
                amount = stone_map[stone]

                if stone == 0:
                    stones[1] += amount
                    continue

                power10 = ceil(log10(stone+1))
                if power10 % 2 == 0:
                    power = 10**(power10//2)
                    stone1 = stone // power
                    stone2 = stone - stone1 * power
                    self.addStone(stones, stone1, amount)
                    self.addStone(stones, stone2, amount)

                else:
                    self.addStone(stones, stone*2024, amount)

            stone_map = stones

        return sum(stone_map.values())

    def solvePartOne(self, data):
        return self.multiplyStones(data, 25)

    def solvePartTwo(self, data):
        return self.multiplyStones(data, 75)


Day11(11).getResults(testOnly=False)
