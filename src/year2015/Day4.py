from src.PythonFramework.Day import Day

import hashlib


class Solver(Day):
    def solvePartOne(self, data):
        i = 0
        key = data[0]
        while True:
            string = key+str(i)
            attempt = hashlib.md5(string.encode())
            if attempt.hexdigest()[0:5] == '00000':
                return i
            i += 1

    def solvePartTwo(self, data):
        i = 0
        key = data[0]
        while True:
            string = key+str(i)
            attempt = hashlib.md5(string.encode())
            if attempt.hexdigest()[0:6] == '000000':
                return i
            i += 1
