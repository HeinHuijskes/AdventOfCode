from src.PythonFramework.Day import Day


class Day11(Day):
    monkeys = dict()

    def solvePartOne(self, data):
        return self.solve(data, divide=3, turns=20)

    def solvePartTwo(self, data):
        # return self.solve(data, divide=1, turns=10000)
        return 'Make me more efficient please!'

    def solve(self, data, divide, turns):
        self.parseInput(data, divide=divide)
        for i in range(0, turns):
            for m in range(0, len(self.monkeys)):
                # if i % 100 == 0:
                #     print(i)
                self.monkeys[m].doTurn()

        activity = []
        for m in range(0, len(self.monkeys)):
            activity.append((self.monkeys[m].inspects, m))
        activity = sorted(activity)
        activity.reverse()
        return activity[0][0] * activity[1][0]

    def parseInput(self, data, divide):
        for i in range(0, len(data), 7):
            monkey = int(data[i].split('Monkey ')[1].split(':')[0])
            items = [int(item) for item in data[i+1].split('Starting items: ')[1].split(', ')]
            operation = data[i+2].split('Operation: ')[1]
            test = int(data[i+3].split('Test: divisible by ')[1])
            next_true = int(data[i+4].split('If true: throw to monkey ')[1])
            next_false = int(data[i+5].split('If false: throw to monkey ')[1])
            self.monkeys[monkey] = self.Monkey(items, operation, test, next_true, next_false, divide)

    def doOperation(self, operation, item):
        operations = operation.split(' ')
        variables, operand = [operations[2], operations[4]], operations[3]
        for i in range(0, len(variables)):
            if variables[i].isnumeric():
                variables[i] = int(variables[i])
            else:
                variables[i] = item
        if operand == '*':
            return variables[0] * variables[1]
        else:
            return sum(variables)

    def doTest(self, monkey, item):
        next_monkey = monkey.next_false
        if item % monkey.test == 0:
            next_monkey = monkey.next_true
        self.monkeys[next_monkey].receiveItem(item)

    class Monkey:
        items = []
        operation = ''
        test = ''
        next_true = 0
        next_false = 0
        inspects = 0
        divide = 3

        def __init__(self, items, operation, test, next_true, next_false, divide):
            self.items = items
            self.operation = operation
            self.test = test
            self.next_true = next_true
            self.next_false = next_false
            self.divide = divide

        def doTurn(self):
            while self.items:
                self.inspect()

        def inspect(self):
            self.inspects += 1
            item = self.items[0]
            self.items = self.items[1:]
            item = Day11().doOperation(self.operation, item)
            item = item // self.divide
            Day11().doTest(self, item)

        def receiveItem(self, item):
            self.items.append(item)


Day11().getResult()
