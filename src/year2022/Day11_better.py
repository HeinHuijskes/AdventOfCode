from src.PythonFramework.Day import Day


class Day11(Day):
    # Each monkey is a tuple containing (operations, test, next_true, next_false)
    monkeys = []
    inspects = []
    items = []
    product = 1

    def parseOperations(self, operations):
        variables, operand = [operations[2], operations[4]], operations[3]
        for i in range(0, len(variables)):
            if variables[i].isnumeric():
                variables[i] = int(variables[i])
        return [variables[0], operand, variables[1]]

    def parse(self, data):
        for i in range(0, len(data), 7):
            items = [int(item) for item in data[i+1].split('Starting items: ')[1].split(', ')]
            operations = self.parseOperations(data[i+2].split('Operation: ')[1].split(' '))
            test = int(data[i+3].split('Test: divisible by ')[1])
            next_true = int(data[i+4].split('If true: throw to monkey ')[1])
            next_false = int(data[i+5].split('If false: throw to monkey ')[1])
            self.monkeys.append((operations, test, next_true, next_false))
            self.items.append(items)

    def generateModulusProduct(self, moduli):
        self.product = 1
        for modulus in moduli:
            self.product *= modulus

    def doTest(self, monkey, item):
        next_monkey = monkey[3]
        if item % monkey[1] == 0:
            next_monkey = monkey[2]
        return next_monkey, item % self.product

    def doOperation(self, operations, item):
        a, b = operations[0], operations[2]
        if not isinstance(a, int):
            a = item
        if not isinstance(b, int):
            b = item
        if operations[1] == '*':
            return a * b
        else:
            return a + b

    def inspect(self, monkey):
        self.inspects[monkey] += 1
        item = self.items[monkey][0]
        self.items[monkey] = self.items[monkey][1:]
        item = self.doOperation(self.monkeys[monkey][0], item)
        next_monkey, item = self.doTest(self.monkeys[monkey], item)
        self.items[next_monkey].append(item)

    def solvePartOne(self, data):
        return 'No part 1 solution yet'

    def solvePartTwo(self, data):
        self.parse(data)
        moduli = list(zip(*self.monkeys))
        self.generateModulusProduct(moduli[1])
        self.inspects = [0 for i in range(0, len(self.monkeys))]
        for i in range(0, 10000):
            if i % 200 == 0:
                print('solved', i)
            for m in range(0, len(self.monkeys)):
                while self.items[m]:
                    self.inspect(m)

        top = sorted(list(zip(self.inspects, [x for x in range(0, len(self.inspects))])))
        top.reverse()
        print(top)
        return top[0][0] * top[1][0]


Day11().getResult()
