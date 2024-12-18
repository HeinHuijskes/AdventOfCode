def getResult():
    data = open('data.txt', 'r').read()
    print(solvePartOne(data))
    print(solvePartTwo(data))


def solvePartOne(data):
    stacks_list, instructions = data.split('\n\n')
    stacks_list = stacks_list.split('\n 1')[0].split('\n')
    instructions = instructions.split('\n')[:-1]

    stacks = [list() for i in range(0, (len(stacks_list[0])+5) // 4)]
    for layer in stacks_list:
        i = 0
        stack = 1
        for i in range(0, len(layer)):
            char = layer[i]
            if i % 4 == 0:
                if char == '[':
                    stacks[stack].append(layer[i+1])
                stack += 1

    for stack in stacks:
        stack.reverse()

    for instruction in instructions:
        x = int(instruction.split('move ')[1].split(' from')[0])
        y = int(instruction.split('from ')[1].split(' to')[0])
        z = int(instruction.split('to ')[1])
        for i in range(0, x):
            stacks[z].append(stacks[y].pop())

    result = ''
    for stack in stacks:
        if stack:
            result += stack.pop()
    return result


def solvePartTwo(data):
    stacks_list, instructions = data.split('\n\n')
    stacks_list = stacks_list.split('\n 1')[0].split('\n')
    instructions = instructions.split('\n')[:-1]

    stacks = [list() for i in range(0, (len(stacks_list[0]) + 5) // 4)]
    for layer in stacks_list:
        i = 0
        stack = 1
        for i in range(0, len(layer)):
            char = layer[i]
            if i % 4 == 0:
                if char == '[':
                    stacks[stack].append(layer[i + 1])
                stack += 1

    for stack in stacks:
        stack.reverse()

    for instruction in instructions:
        x = int(instruction.split('move ')[1].split(' from')[0])
        y = int(instruction.split('from ')[1].split(' to')[0])
        z = int(instruction.split('to ')[1])
        stacky = list()
        for i in range(0, x):
            stacky.append(stacks[y].pop())
        stacky.reverse()
        for box in stacky:
            stacks[z].append(box)

    result = ''
    for stack in stacks:
        if stack:
            result += stack.pop()
    return result


getResult()
