import sys
sys.path.append('../../../src')

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
                break
            else:
                i += 1
        return i

    def solvePartTwo(self, data):
        i = 0
        key = data[0]
        while True:
            string = key+str(i)
            attempt = hashlib.md5(string.encode())
            if attempt.hexdigest()[0:6] == '000000':
                break
            else:
                i += 1
        return i


Day4().getResult()
