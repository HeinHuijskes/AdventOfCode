from src.PythonFramework.Day import Day


class Solver(Day):
    def assessCharacter(self, char, line, i):
        number = 0
        if char == '-' or char.isnumeric():
            number = char
            j = 1
            while i+j < len(line) and line[i+j].isnumeric():
                number += line[i+j]
                j += 1
            number = int(number)
            i += j
        else:
            i += 1
        return number, i

    def solvePartOne(self, data):
        line = data[0]
        total = 0
        i = 0
        while i < len(line):
            number, i = self.assessCharacter(line[i], line, i)
            total += number
        return total
    
    def checkObject(self, line, i):
        hasRed = False
        subTotal = 0
        while i < len(line):
            char = line[i]
            if char == '{':
                number, i = self.checkObject(line, i+1)
                subTotal += number
            else:
                if char == '"':
                    if i+3 < len(line):
                        if line[i+1:i+4] == 'red' and line[i-1] == ':':
                            hasRed = True
                    i += 1
                else:
                    number, i = self.assessCharacter(char, line, i)
                    subTotal += number
            if char == '}':
                break
        if hasRed:
            subTotal = 0
        return subTotal, i

    def solvePartTwo(self, data):
        line = data[0]
        total = 0
        i = 0
        while i < len(line):
            char = line[i]
            if char == '{':
                number, i = self.checkObject(line, i+1)
            else:
                number, i = self.assessCharacter(char, line, i)
            total += number
        return total
