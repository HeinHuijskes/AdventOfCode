import sys
sys.path.append('../../../src')
sys.setrecursionlimit(10000)

from PythonFramework.Day import Day


def getDirection(piece, coords, direction):
    x, y = coords
    # Direction means the current direction that the piece lies in compared to the current coordinates
    # Returned are the coordinates of the considered piece, and the new direction that it points in
    dx, dy = direction
    if piece == '|':
        if dx == 0 and dy != 0:
            return (x + dx, y + dy), (dx, dy)
    if piece == '-':
        if dx != 0 and dy == 0:
            return (x + dx, y + dy), (dx, dy)
    if piece == 'F':
        if dx == 0 and dy == -1:
            return (x + dx, y + dy), (1, 0)
        if dx == -1 and dy == 0:
            return (x + dx, y + dy), (0, 1)
    if piece == 'L':
        if dx == 0 and dy == 1:
            return (x + dx, y + dy), (1, 0)
        if dx == -1 and dy == 0:
            return (x + dx, y + dy), (0, -1)
    if piece == '7':
        if dx == 0 and dy == -1:
            return (x + dx, y + dy), (-1, 0)
        if dx == 1 and dy == 0:
            return (x + dx, y + dy), (0, 1)
    if piece == 'J':
        if dx == 0 and dy == 1:
            return (x + dx, y + dy), (-1, 0)
        if dx == 1 and dy == 0:
            return (x + dx, y + dy), (0, -1)
    return None, None


def getMainLoop(data):
    x, y = 0, 0
    main_loop = []
    grid = []
    for i, line in enumerate(data):
        grid.append([])
        for j, pipe in enumerate(line):
            grid[i].append(pipe)
            if pipe == 'S':
                y, x = i, j
    start = [x,y,()]
    foundStart = False
    coords, direction = None, None
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i == j == 0) or (i != 0 and j != 0):
                continue
            # The dataset only connects to 'S' twice, so there are no false starts possible
            coords, direction = getDirection(grid[y+i][x+j], (x, y), (j, i))
            if coords != None:
                x, y = coords
                main_loop.append((x,y,direction))
                foundStart = True
                break
        if foundStart:
            break
    
    piece = grid[y+direction[1]][x+direction[0]]
    while piece != 'S':
        (x,y), direction = getDirection(piece, (x, y), direction)
        main_loop.append((x,y,direction))
        piece = grid[y+direction[1]][x+direction[0]]
    start[2] = (main_loop[0][0] - start[0], main_loop[0][1] - start[1])
    main_loop.append(start)
    return main_loop


def expandOutside(x, y, visited):
    visited[y][x] = True
    if x > 0 and not visited[y][x-1]:
        expandOutside(x-1, y, visited)
    if x < len(visited[0])-1 and not visited[y][x+1]:
        expandOutside(x+1, y, visited)
    if y > 0 and not visited[y-1][x]:
        expandOutside(x, y-1, visited)
    if y < len(visited)-1 and not visited[y+1][x]:
        expandOutside(x, y+1, visited)
    return


class Day10(Day):
    def solvePartOne(self, data):
        main_loop = getMainLoop(data)
        return (len(main_loop))//2

    def solvePartTwo(self, data):
        # Initialize some values
        main_loop = getMainLoop(data)
        visited = [[False for i in range(len(data[0]))] for j in range(len(data))]
        for x, y, direction in main_loop:
            visited[y][x] = True
        outside = []

        # Find the topleft value and use it as a new starting point
        # This is my scuffed way of making sure we rotate in the correct direction
        index = 0
        topleft = main_loop[0]
        for i, pipe in enumerate(main_loop):
            if pipe[0] <= topleft[0] and pipe[1] <= topleft[1]:
                topleft = pipe
                index = i
        main_loop = main_loop[index:] + main_loop[:index]
        # Check what direction we are rotating in
        if topleft[2] == (0, 1):
            # Down (counterclockwise)
            rotationMap = {(0, -1): (1, 0), (-1, 0): (0, -1), (0, 1): (-1, 0), (1, 0): (0, 1)}
        elif topleft[2] == (1, 0):
            # Right (clockwise)
            rotationMap = {(0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1)}
        else:
            print('???')

        pipeMap = {'F': ((-1, 0), (0, -1)), 'J': ((1, 0), (0, 1)), '7': ((1, 0), (0, -1)), 'L': ((-1, 0), (0, 1))}
        # Walk along the path clockwise, and mark the "outside" on the left
        for x, y, direction in main_loop:
            outsideChecks = [rotationMap[direction]]
            if data[y][x] in 'FJ7L' and outsideChecks[0] in pipeMap[data[y][x]]:
                outsideChecks.append(rotationMap[outsideChecks[0]])
            for outCheck in outsideChecks:
                dx, dy = outCheck
                lx, ly = x+dx, y+dy
                if (lx >= 0 and ly >= 0 and lx < len(data[0]) and ly < len(data)) and not visited[ly][lx]:
                    outside.append((lx, ly))

        for x, y in outside:
            if not visited[y][x]:
                expandOutside(x, y, visited)
        
        loop = [(x,y) for x,y,a in main_loop]
        inside = 0
        for y in range(len(visited)):
            line = ''
            for x in range(len(visited[0])):
                if (x,y) == (4,0):
                    print('here', (x,y) in loop)
                if (x,y) in outside:
                    line += '\033[1;34;40m*\033[0m'
                elif (x,y) in loop:
                    line += data[y][x]
                elif visited[y][x]:
                    line += ' '
                else:
                    line += '\033[1;31;40mx\033[0m'
                    inside += 1
            print(line)

        return inside


Day10().getResult(testOnly=False)
