class Day:
    def getResult(self, testOnly = False):
        test_data = open('testdata.txt', 'r').read()
        if len(test_data) > 0:
            test_data = test_data.split('\n')[:-1]
            print('Test answer part 1:', self.solvePartOne(test_data))
            print('Test answer part 2:', self.solvePartTwo(test_data))

        if testOnly:
            return
        data = open('data.txt', 'r').read().split('\n')[:-1]
        print('Answer part 1:', self.solvePartOne(data))
        print('Answer part 2:', self.solvePartTwo(data))

    def solvePartOne(self, data):
        return 'No part 1 solution yet'

    def solvePartTwo(self, data):
        return 'No part 2 solution yet'
