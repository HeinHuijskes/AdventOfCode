from src.PythonFramework.Day import Day


class Solver(Day):
    def parse(self, data):
        return data

    def solvePartOne(self, data):
        difference = len(data)*2  # All outside quote strings
        hexchars = '0123456789abcdef'
        for line in data:
            i = 0
            while i < len(line):
                char = line[i]
                if char == '\\':
                    if line[i+1] == '\\' or line[i+1] == '"':
                        difference += 1
                        i += 1
                    elif line[i+1] == "x" and i < len(line)-2:
                        if line[i+2] in hexchars and line[i+3] in hexchars:
                            difference += 3
                            i += 3
                i += 1
        return difference

    def solvePartTwo(self, data):
        difference = len(data)*2  # All outside quote strings
        for line in data:
            for char in line:
                if char == '\\' or char == '"':
                    difference += 1
        return difference
