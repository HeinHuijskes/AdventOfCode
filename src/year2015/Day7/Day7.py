import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day


gates = ['AND', 'LSHIFT', 'RSHIFT', 'NOT', 'OR']
separator = '->'


def parse(commands, variables):
    # Set up the network as sort of nodes
    input1 = None
    input2 = None
    gate = None
    output = commands[-1]
    for command in commands:
        if command == separator:
            break
        elif command in gates:
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


def performOperation(output, variables, visited):
    input1, input2, gate = variables[output]
    result = None
    if gate == None and isinstance(input1, str):
        input1 = performOperation(input1, variables, visited)
    if isinstance(input1, str):
        input1 = performOperation(input1, variables, visited)
    if isinstance(input2, str):
        input2 = performOperation(input2, variables, visited)
    
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


class Day7(Day):
    def solvePartOne(self, data):
        variables = {}
        for line in data:
            commands = line.split(' ')
            parse(commands, variables)
        return performOperation('a', variables, [])

    def solvePartTwo(self, data):
        a = self.solvePartOne(data)
        variables = {}
        for line in data:
            commands = line.split(' ')
            parse(commands, variables)
        variables['b'] = (a, None, None)
        return performOperation('a', variables, [])


Day7().getResult()
