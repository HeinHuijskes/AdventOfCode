from src.PythonFramework.Day import Day
import src.PythonFramework.Algorithms as algs


class Solver(Day):
    test_answers = [357, 3121910778619]
    answers = [17321, 171989894144198]

    def parse(self, data: list[str]):
        return [[int(battery) for battery in bank] for bank in data]
    
    def solve(self, data, num_batteries):
        total = 0
        for bank in data:
            # Find the highest possible number, given that we still need i batteries afterwards
            for i in reversed(range(num_batteries)):
                short_bank = bank[:-i]
                if i == 0: short_bank = bank
                top = max(short_bank)
                index = bank.index(top)
                bank = bank[index+1:]
                total += 10**i * top
        return total

    def solvePartOne(self, data: list[list[int]]):
        return self.solve(data, 2)

    def solvePartTwo(self, data):
        return self.solve(data, 12)
