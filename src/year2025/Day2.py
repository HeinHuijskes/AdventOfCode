from src.PythonFramework.Day import Day
import src.PythonFramework.Algorithms as algs


class Solver(Day):
    test_answers = [1227775554, 4174379265]
    answers = [35367539282, 45814076230]

    def parse(self, data: list[str]):
        # Return a list of tuples with first and last id: [(first1, last1), (first2, last2), ...]
        return [(int(a),int(b)) for a,b in map(lambda x: x.split('-'), data[0].split(','))]

    def solvePartOne(self, data):
        result = 0
        for a, b in data:
            for x in range(a, b+1):
                number = str(x)
                # Check for each number in a range that both halves are equal
                if number[:len(number)//2] == number[len(number)//2:]:
                    result += x
        return result
    
    def hasMultiples(self, number):
        maximum = len(number)//2
        # Consider chunks of length i of a number
        for i in range(1, maximum+1):
            chunks = len(number) // i
            if not chunks * i == len(number):
                continue
            chunk = number[0:i]
            if chunk*chunks == number:
                return True
        return False

    def solvePartTwo(self, data):
        result = 0
        for a, b in data:
            for x in range(a, b+1):
                # Now check all posible multiples in x
                if self.hasMultiples(str(x)):
                    result += x
        return result
