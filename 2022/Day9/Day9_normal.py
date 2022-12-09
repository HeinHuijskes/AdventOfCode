import time


def getResult():
    test_data = open('testdata.txt', 'r').read()
    if len(test_data) > 0:
        test_data = test_data.split('\n')[:-1]
        print('Test answer part 1:', solvePartOne(test_data))
        print('Test answer part 2:', solvePartTwo(test_data))

    data = open('data.txt', 'r').read().split('\n')[:-1]
    print('Answer part 1:', solvePartOne(data))
    print('Answer part 2:', solvePartTwo(data))


def parseMoves(data):
    moves = []
    for line in data:
        x, y = 0, 0
        direction, amount = line.split(' ')
        if direction == 'R':
            x += int(amount)
        if direction == 'L':
            x -= int(amount)
        if direction == 'U':
            y -= int(amount)
        if direction == 'D':
            y += int(amount)
        moves.append((x, y))
    return moves


def trackMoves(moves, knots=2):
    tail_visited = {(0, 0): True}
    positions = []
    for i in range(0, knots):
        positions.append((0, 0))
    head = len(positions)-1

    for (x, y) in moves:
        divider = max(abs(x), abs(y))
        for i in range(0, divider):
            positions[head] = ((positions[head][0] + x//divider), (positions[head][1] + y//divider))
            # display(positions)
            moveTail(positions)
            display(positions)
            tail_visited[positions[0]] = True

    return len(tail_visited)


def moveTail(positions):
    for i in reversed(range(1, len(positions))):
        (knot_x, knot_y) = positions[i - 1]
        (head_x, head_y) = positions[i]
        diff_x = head_x - knot_x
        diff_y = head_y - knot_y

        if abs(diff_x) > 1:
            knot_x += diff_x // 2
            if abs(diff_y) == 1:
                knot_y += diff_y

        if abs(diff_y) > 1:
            knot_y += diff_y // 2
            if abs(diff_x) == 1:
                knot_x += diff_x

        positions[i - 1] = (knot_x, knot_y)
    return positions


def display(positions, center='tail', delay=0.1):
    # In the display grid, the head is always located in the middle
    strings = []
    size = len(positions)*2 + 1
    for y in reversed(range(0, size)):
        strings.append('')
        for x in range(0, size):
            strings[size-y-1] += getCharacter(x, y, size, positions, center=center)
    for string in strings:
        print(string)
    print()
    time.sleep(delay)


def getCharacter(x, y, size, positions, center):
    if center == 'head':
        center = len(positions)-1
    elif center == 'tail':
        center = 0
    (center_x, center_y) = positions[center]
    mid_x, mid_y = size//2, size//2
    result = '#'
    for i in range(0, len(positions)):
        position = positions[i]
        rel_x = mid_x + position[0] - center_x
        rel_y = mid_y + position[1] - center_y
        if rel_x == x and rel_y == y:
            result = str(i)
    return result


def solvePartOne(data):
    moves = parseMoves(data)
    return trackMoves(moves)


def solvePartTwo(data):
    moves = parseMoves(data)
    return trackMoves(moves, knots=10)


getResult()
