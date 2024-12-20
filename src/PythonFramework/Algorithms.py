# def bsearch(self, list, item):
#     # Binary search
#     return None

# def gridSearch(self, grid, item):
#     return None

# def gridGetLine(self, grid, x, y, length=-1, directions = [(0, 1), (1, 1), (1, 0), (-1, 0), (-1, -1), (0, -1), (-1, 1), (1, -1)]):
#     return None

# def gridSnakeSearch(self, grid, x, y, condition):
#     return None

# def gridAStar(self, grid, x, y, target):
#     return None

def gridify(data, wall='#'):
    '''Returns a boolean grid parsed from a string grid'''
    return [[char != wall for char in line] for line in data]

def findDimensions(a):
    '''Returns the dimensions of a multi-dimensional array, assuming uniformity'''
    if not type(a) == list:
        return 1
    return 1 + findDimensions(a[0])

def findvalues(data, values):
    '''Returns coordinates for the first occurence of values in a multi-dimensional array'''
    dimensions = findDimensions(data)
    return [findvalue(data, value, dimensions) for value in values]

def findvalue(data, value, dimensions=2):
    '''Returns coordinates for the first occurence of a value in a multi-dimensional array'''
    if dimensions == 1:
        if value in data:
            return [data.index(value)]
        return None
    for i, line in enumerate(data):
        index = findvalue(line, value, dimensions=dimensions-1)
        if index != None:
            return index + [i]

def dijkstra(grid: list[list], x: int, y: int, gx: int, gy: int) -> list[tuple[int, int, int]]:
    '''
    Returns the fastest path according to Dijkstra\'s algorithm.
    Each node in the path points to the coordinates of the node on the grid, and has a score based on manhattan distance.
    '''
    def getNeighbours(grid, x, y, visited):
        '''Return neighbours of a node. They must be in bounds, not impassible on the grid, and not visited yet.'''
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        lim_x, lim_y = len(grid[0]), len(grid)
        return [(x+dx, y+dy) for dx, dy in directions 
                if 0 <= x+dx < lim_x and 0 <= y+dy < lim_y 
                and grid[y+dy][x+dx] and visited[y+dy][x+dx] == None]

    nodes = [[None for i in range(len(grid[0]))] for j in range(len(grid))]
    nodes[y][x] = (x, y, 0)
    queue = [(x, y, 0)]
    while len(queue) != 0:
        x, y, score = queue.pop(0)
        if (x == gx and y == gy):
            break
        neighbours = getNeighbours(grid, x, y, nodes)
        for nx, ny in neighbours:
            queue.append((nx, ny, score+1))
            nodes[ny][nx] = (x, y, score+1)
    (px, py, score) = nodes[gy][gx]
    path = [(gx, gy, score+1)]
    while score != 0:
        path.append((px, py, score))
        (px, py, score) = nodes[py][px]

    return path
