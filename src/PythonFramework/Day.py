import src.PythonFramework.Algorithms as alg
import time
import os

class Day:
    day = 0
    start_time = 0
    total_time = 0
    testanswer1, testanswer2 = None, None
    answer1, answer2 = None, None

    def __init__(self, day=0, year=0) -> None:
        self.day = day
        self.year = year

    def displayAnswer(self, part, correct, solver, input, test=False, decimals = 4):
        self.start_time = time.perf_counter()
        answer = solver(input)
        time_taken = time.perf_counter() - self.start_time
        self.total_time += time_taken
        result = ['incorrect', 'correct'][answer == correct and answer != None]
        string = f'Answer {part} - {answer} ({result}) [{round(time_taken, 4)} sec]'
        if test:
            string = f'[Test] {string}'
        print(string)

    def getResult(self, test=False, normal=True, testOnly=False):
        if testOnly:
            test, normal = True, False
        data_path = f'./src/data/year{self.year}/Day{self.day}'
        self.start_time = time.perf_counter()
        if test:
            test_data = open(f'{data_path}/testdata.txt', 'r').read()
            if len(test_data) > 0:
                test_data_1 = self.parseTest(test_data.split('\n')[:-1])
                test_data_2 = self.parseTest(test_data.split('\n')[:-1])
                self.displayAnswer(1, self.testanswer1, self.solvePartOne, test_data_1, test=True)
                self.displayAnswer(2, self.testanswer2, self.solvePartTwo, test_data_2, test=True)

        if normal:
            data_1 = self.parse(open(f'{data_path}/data.txt', 'r').read().split('\n')[:-1])
            data_2 = self.parse(open(f'{data_path}/data.txt', 'r').read().split('\n')[:-1])
            self.displayAnswer(1, self.answer1, self.solvePartOne, data_1)
            self.displayAnswer(2, self.answer2, self.solvePartTwo, data_2)
        print(f'Total time: {round(self.total_time, 4)} sec')

    def parse(self, data):
        return data
    
    def parseTest(self, data):
        return self.parse(data)

    def solvePartOne(self, data):
        return None

    def solvePartTwo(self, data):
        return None
