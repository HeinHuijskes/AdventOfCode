from src.PythonFramework.Day import Day

from regex import regex as re


class Solver(Day):
    def parse(self, data):
        items = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
        Sues = [{} for i in range(500)]
        for line in data:
            # There are always 3 characteristics given for any Sue
            groups = re.match('Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', line).groups()
            sue = int(groups[0])-1
            for i in range(3):
                Sues[sue][groups[1+2*i]] = int(groups[2+2*i])
        return items, Sues
    
    def isTheSue(self, Sues, Sue, items):
        for item in Sues[Sue]:
            if Sues[Sue][item] != items[item]:
                return False
        return True
    
    def isTheRealSue(self, Sues, Sue, items):
        for item in Sues[Sue]:
            if item == 'cats' or item == 'trees':
                if Sues[Sue][item] <= items[item]:
                    return False
            elif item == 'pomeranians' or item == 'goldfish':
                if Sues[Sue][item] >= items[item]:
                    return False
            else:
                if Sues[Sue][item] != items[item]:
                    return False
        return True

    def solvePartOne(self, data):
        items, Sues = data
        for Sue in range(len(Sues)):
            if self.isTheSue(Sues, Sue, items):
                return Sue+1

    def solvePartTwo(self, data):
        items, Sues = data
        for Sue in range(len(Sues)):
            if self.isTheRealSue(Sues, Sue, items):
                return Sue+1
