from src.PythonFramework.Day import Day

import hashlib

class Solver(Day):
    answers = ['c6697b55', '8c35d1ab']
    hashes = []
    i = 0
    def parse(self, data):
        return data[0]
    
    def getHash(self, data):
        while True:
            string = data+str(self.i)
            attempt = hashlib.md5(string.encode())
            result = attempt.hexdigest()
            self.i += 1
            if result[0:5] == '00000':
                self.hashes.append(result)
                break

    def solvePartOne(self, data):
        password = []
        for j in range(8):
            self.getHash(data)
            password.append(self.hashes[-1][5])
        return ''.join(password)
    
    def addToPassword(self, hash, password):
        position = int(hash[5], 16)
        if position < 8 and password[position] == None:
            password[position] = hash[6]

    def solvePartTwo(self, data):
        password = [None for i in range(8)]
        for hash in self.hashes:
            self.addToPassword(hash, password)
        while None in password:
            self.getHash(data)
            self.addToPassword(self.hashes[-1], password)
        return ''.join(password)
