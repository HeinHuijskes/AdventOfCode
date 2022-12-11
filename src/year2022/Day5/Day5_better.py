import re as regex


def getResult():
    data = open('data.txt', 'r').read().split('\n')[:-1]
    print(solvePartOne(data))
    print(solvePartTwo(data))


def solvePartOne(data):
    # Separate the instructions and the initial state of crates
    instructions, initial = data[10:], data[:9]
    # Prepare an array to store the stacks of crates in
    crates = [[] for i in range(0, (len(initial[0]) + 1) // 4)]
    # Parse the current state of crates and store in the stacks
    for x in range(1, len(initial[0]), 4):
        for y in range(0, len(initial)):
            if initial[y][x] != ' ':
                index = (x - 1) // 4
                crates[index].insert(0, initial[y][x])
    # Parse the instructions and apply them to the stacks
    for instruction in instructions:
        # Regex that returns the numbers in a string
        [times, origin, destination] = [regex.findall(r'\d+', instruction)]
        times, origin, destination = list(map(int, [times, origin, destination]))
        for i in range(0, times):
            crates[destination-1].append(crates[origin-1].pop())
    # Collect the top of each array in the stack in a list, and join them together
    return ''.join([stack.pop() for stack in crates])


def solvePartTwo(data):
    # Same as part 1
    instructions, initial = data[10:], data[:9]
    crates = [[] for i in range(0, (len(initial[0]) + 1) // 4)]
    for x in range(1, len(initial[0]), 4):
        for y in range(0, len(initial)):
            if initial[y][x] != ' ':
                index = (x - 1) // 4
                crates[index].insert(0, initial[y][x])
    # Parse the instructions and apply them to the stacks
    for instruction in instructions:
        times, origin, destination = regex.findall(r'\d+', instruction)
        times, origin, destination = int(times), int(origin), int(destination)
        # Add a boxes array to temporarily store the boxes that are being moved
        boxes = []
        for i in range(0, times):
            boxes.append(crates[origin - 1].pop())
        # The list has to be reversed since the boxes are popped off a stack normally, placing them in reverse order
        for box in list(reversed(boxes)):
            crates[destination - 1].append(box)
    return ''.join([c.pop() for c in crates])


getResult()
