import sys
sys.path.append('../../src')

import hashlib

from PythonFramework.Day import Day


class Day4(Day):
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


Day4(4).getResult()
