from src.PythonFramework.Day import Day
from regex import regex, compile


class Solver(Day):
    testanswer1, testanswer2 = 2, 3
    answer1, answer2 = 110, 242

    def parse(self, data):
        return data
    
    def solve(self, data, finder: regex.Pattern, part2=False):
        splitter = compile(f'\[|\]')
        result = 0
        for line in data:
            split_line = splitter.split(line)
            supernet, hypernet = [], []
            for i in range(len(split_line)):
                sequence = [string for string in finder.findall(split_line[i], overlapped=True) if string[0] != string[1]]
                if i % 2 == 0:
                    supernet += sequence
                else:
                    hypernet += sequence
            if not part2:
                result += len(hypernet) == 0 and len(supernet) > 0
            else:
                result += self.supportsSSL(supernet, hypernet)
        return result
    
    def supportsSSL(self, supernet: str, hypernet: str):
        for b, a, b in hypernet:
            for aba in supernet:
                if a == aba[0] and b == aba[1]:
                    return True
        return False

    def solvePartOne(self, data):
        return self.solve(data, finder=compile(r'(\w)(\w)(\2)(\1)'))

    def solvePartTwo(self, data):
        return self.solve(data, finder=compile(r'(\w)(\w)(\1)'), part2=True)
