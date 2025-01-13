from src.PythonFramework.Day import Day


class Day13(Day):
    def parse(self, data):
        As, Bs, totals = [], [], []
        for i in range(0, len(data), 4):
            As.append([int(x[2:]) for x in data[i][9:].split(', ')])
            Bs.append([int(x[2:]) for x in data[i+1][9:].split(', ')])
            totals.append([int(x[2:]) for x in data[i+2][7:].split(', ')])
        return As, Bs, totals
    
    def findOptimum(self, A, B, total):
        (x_A, y_A), (x_B, y_B), (x_total, y_total) = A, B, total
        b = (x_total - y_total*x_A/y_A) / (x_B - y_B*x_A/y_A)
        a = (y_total - b*y_B) / y_A
        return a, b

    def calculateTokens(self, data, add=0):
        As, Bs, totals = data
        totals = [(x+add, y+add) for x, y in totals]
        result = 0
        margin = 0.001
        for i in range(len(As)):
            A, B, total = As[i], Bs[i], totals[i]
            a, b = self.findOptimum(A, B, total)
            # Check value is between margins to avoid cpu rounding error
            if a-margin <= round(a) <= a+margin and b-margin <= round(b) <= b+margin:
                result += round(a)*3 + round(b)
        return int(result)

    def solvePartOne(self, data):
        return self.calculateTokens(data)

    def solvePartTwo(self, data):
        return self.calculateTokens(data, add=10000000000000)
