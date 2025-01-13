from src.PythonFramework.Day import Day


class Solver(Day):
    gates = ['AND', 'LSHIFT', 'RSHIFT', 'NOT', 'OR']
    separator = '->'

    def parseCommands(self, commands, variables):
        # Set up the network as sort of nodes
        input1 = None
        input2 = None
        gate = None
        output = commands[-1]
        for command in commands:
            if command == self.separator:
                break
            elif command in self.gates:
                gate = command
            else:
                if input1 == None:
                    if command.isnumeric():
                        input1 = int(command)
                    else:
                        input1 = command
                else:
                    if command.isnumeric():
                        input2 = int(command)
                    else:
                        input2 = command
        variables[output] = (input1, input2, gate)

    def performOperation(self, output, variables, visited):
        input1, input2, gate = variables[output]
        result = None
        if gate == None and isinstance(input1, str):
            input1 = self.performOperation(input1, variables, visited)
        if isinstance(input1, str):
            input1 = self.performOperation(input1, variables, visited)
        if isinstance(input2, str):
            input2 = self.performOperation(input2, variables, visited)
        
        if gate == None:
            result = input1
        elif gate == 'AND':
            result = input1 & input2
        elif gate == 'LSHIFT':
            result = input1 << input2
        elif gate == 'RSHIFT':
            result = input1 >> input2
        elif gate == 'NOT':
            result = ~ input1
        elif gate == 'OR':
            result = input1 | input2
        else:
            return None
        
        # Prune branches to avoid recalculating numbers by overriding entries for known outputs
        variables[output] = (result, None, None)
        return result
    def solvePartOne(self, data):
        variables = {}
        for line in data:
            commands = line.split(' ')
            self.parseCommands(commands, variables)
        return self.performOperation('a', variables, [])

    def solvePartTwo(self, data):
        a = self.solvePartOne(data)
        variables = {}
        for line in data:
            commands = line.split(' ')
            self.parseCommands(commands, variables)
        variables['b'] = (a, None, None)
        return self.performOperation('a', variables, [])
