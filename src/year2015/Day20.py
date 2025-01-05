import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Day20(Day):
    def parse(self, data):
        return int(data[0])
    
    def getLimit(self, data):
        # House 2^k always has the new highest presents value for previous houses, so it is safe to use as a limit
        # Also: house 2^k gets 2^(k+1)-1 presents, so look for 2^k where 2^(k+1)-1 >= data
        k = 1
        while 2**(k+1)-1 < data:
            k += 1
        return 2**k

    def solvePartOne(self, data):
        data = data//10
        limit = self.getLimit(data)
        array = [1 for i in range(limit)]
        for house in range(2, limit):
            # Index has to be offset by 1, since houses start at 1 and not 0
            for j in range(house-1, limit, house):
                # Add the value of the house to subsequent houses up to the limit
                array[j] += house
            if array[house-1] >= data:
                break
        return house

    def solvePartTwo(self, data):
        # Assume the limit is the same as in part one
        limit = self.getLimit(data//10)
        print(limit)
        array = [0 for i in range(limit)]
        for house in range(1, limit):
            for j in range(house-1, min(house-1+50*house, limit), house):
                array[j] += 11*house
            if array[house-1] >= data:
                break
        return house


Day20(20).getResult(testOnly=False)
