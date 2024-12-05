import PythonFramework.Algorithms as Algorithms
import time

class Day:
    day = 0
    start_time = 0
    inter_time = 0

    def __init__(self, day) -> None:
        self.day = day

    def updateTime(self):
        self.inter_time = time.perf_counter() - self.start_time - self.inter_time

    def displayAnswer(self, part, answer, test=False, decimals = 4):
        self.updateTime()
        if test:
            print(f'Test {part}   - {answer}   ({round(self.inter_time, decimals)} sec)')
        else: 
            print(f'Answer {part} - {answer}   ({round(self.inter_time, decimals)} sec)')

    def getResult(self, testOnly = False):
        self.start_time = time.perf_counter()
        test_data = open('./testdata.txt', 'r').read()
        if len(test_data) > 0:
            test_data = self.parse(test_data.split('\n')[:-1])
            self.displayAnswer(1, self.solvePartOne(test_data), test=True)
            self.displayAnswer(2, self.solvePartTwo(test_data), test=True)

        if testOnly:
            return
        data = self.parse(open('./data.txt', 'r').read().split('\n')[:-1])
        self.displayAnswer(1, self.solvePartOne(data))
        self.displayAnswer(2, self.solvePartTwo(data))
        print(f'Total time: {round(time.perf_counter() - self.start_time, 4)} sec')

    def parse(self, data):
        return data

    def solvePartOne(self, data):
        return 'No part 1 solution yet'

    def solvePartTwo(self, data):
        return 'No part 2 solution yet'
