def getResult():
    test_data = open('testdata.txt', 'r').read()
    if len(test_data) > 0:
        test_data = test_data.split('\n')[:-1]
        print('Test answer part 1:', solvePartOne(test_data))
        print('Test answer part 2:', solvePartTwo(test_data))

    data = open('data.txt', 'r').read().split('\n')[:-1]
    print('Answer part 1:', solvePartOne(data))
    print('Answer part 2:', solvePartTwo(data))


def doCycle(cycle, register, result, part2=False):
    if part2:
        pixel = '.'
        if (register - 1) <= ((cycle - 1) % 40) <= (register + 1):
            pixel = '#'
        result.append(pixel)
    elif cycle % 40 == 20:
        result.append(register * cycle)
    return cycle + 1


def draw(screen):
    result = '\n'
    height = 6
    width = len(screen)//height
    for h in range(0, height):
        for w in range(0, width):
            result += screen[h * width + w]
        result += '\n'

    return result


def solvePartOne(data):
    register = 1
    signal_strengths = []
    cycle = 1
    for line in data:
        cycle = doCycle(cycle, register, signal_strengths)
        if 'noop' not in line:
            cycle = doCycle(cycle, register, signal_strengths)
            print(line, line.split())
            register += int(line.split(' ')[1])

    return sum(signal_strengths)


def solvePartTwo(data):
    register = 1
    cycle = 1
    screen = []
    for line in data:
        cycle = doCycle(cycle, register, screen, part2=True)
        if 'noop' not in line:
            cycle = doCycle(cycle, register, screen, part2=True)
            register += int(line.split(' ')[1])

    return draw(screen)


getResult()
