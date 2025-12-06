import src.PythonFramework.Algorithms as alg
from src.PythonFramework.GUI.GUIs import GUI_GETTER
from threading import Thread
import time

class Day:
    day = 0
    start_time = 0
    total_time = 0
    test_answers = [None, None]
    answers = [None, None]
    testOnly, test, normal = False, False, True
    GUI_type: str | None = None

    def __init__(self, day=0, year=0) -> None:
        self.day = day
        self.year = year

        if self.GUI_type != None:
            self.GUI = GUI_GETTER().getGui(self.GUI_type)
            self.gui_thread = Thread(target=self.GUI.runGUI)
            self.gui_thread.start()

    def runAnswer(self, part, correct_answer, solver, input, test=False):
        self.start_time = time.perf_counter_ns()
        answer = solver(input)
        time_taken = time.perf_counter_ns() - self.start_time
        self.total_time += time_taken
        correct = answer == correct_answer and answer != None
        result = ['incorrect', 'correct'][correct]
        string = f'Answer {part} - {answer} ({result}) [{round(time_taken/(10**9), 4)} sec]'
        if test:
            string = f'[Test] {string}'
        return time_taken, correct, string

    def getResult(self, test, part):
        if not test:
            answer = self.answers[part-1]
        else:
            answer = self.test_answers[part-1]
        if part == 1:
            func = self.solvePartOne
        else:
            func = self.solvePartTwo
        data_path = f'./src/data/year{self.year}/Day{self.day}'
        if test:
            data_path = f'{data_path}/testdata.txt'
        else:
            data_path = f'{data_path}/data.txt'
        data = self.parse(open(data_path, 'r').read().split('\n')[:-1])
        return self.runAnswer(part, answer, func, data, test=test)

    def getResults(self):
        if self.testOnly:
            self.test, self.normal = True, False
        if self.test:
            print(self.getResult(test=True, part=1)[2])
            print(self.getResult(test=True, part=2)[2])

        if self.normal:
            print(self.getResult(test=False, part=1)[2])
            print(self.getResult(test=False, part=2)[2])
        print(f'Total time: {round(self.total_time/(10**9), 4)} sec')
        if self.GUI_type != None:
            self.GUI.run = False
            self.gui_thread.join()

    def parse(self, data):
        return data
    
    def parseTest(self, data):
        return self.parse(data)

    def solvePartOne(self, data):
        return None

    def solvePartTwo(self, data):
        return None

    def visualise(self, value):
        self.GUI.update(value)
        return
