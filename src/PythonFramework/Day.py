import time

class Day:
    start_time = 0
    inter_time = 0
    def updateTime(self):
        self.inter_time = time.perf_counter() - self.start_time - self.inter_time

    def displayAnswer(self, part, answer, test=False, timeFactor = 10000):
        self.updateTime()
        if test:
            print(f'Test {part}   ({int(self.inter_time*timeFactor)/timeFactor} sec): {answer}')
        else: 
            print(f'Answer {part} ({int(self.inter_time*timeFactor)/timeFactor} sec): {answer}')

    def getResult(self, testOnly = False):
        self.start_time = time.perf_counter()
        test_data = open('testdata.txt', 'r').read()
        if len(test_data) > 0:
            test_data = test_data.split('\n')[:-1]
            self.displayAnswer(1, self.solvePartOne(test_data), test=True)
            self.displayAnswer(2, self.solvePartTwo(test_data), test=True)

        if testOnly:
            return
        data = open('data.txt', 'r').read().split('\n')[:-1]
        self.displayAnswer(1, self.solvePartOne(data))
        self.displayAnswer(2, self.solvePartTwo(data))
        print(f'Total time: {time.perf_counter() - self.start_time} sec')

    def solvePartOne(self, data):
        return 'No part 1 solution yet'

    def solvePartTwo(self, data):
        return 'No part 2 solution yet'
