from src.PythonFramework.Day import Day


class Solver(Day):
    height_map = []
    a_positions = []
    root = None
    goal = (0, 0)
    width = 0
    height = 0

    def reset(self):
        self.height_map = []
        self.a_positions = []
        self.root = None
        self.goal = (0, 0)
        self.width = 0
        self.height = 0

    class Node:
        x, y = 0, 0
        parent = None

        def __init__(self, x, y, parent):
            self.x, self.y = x, y
            self.parent = parent

    def parseData(self, data):
        self.width = len(data[0])
        self.height = len(data)
        for y in range(0, self.height):
            self.height_map.append([])
            for x in range(0, self.width):
                char = data[y][x]
                self.height_map[y].append(ord(char))
                if char == 'S':
                    self.root = self.Node(x, y, None)
                    self.height_map[y][x] = ord('a')
                if char == 'E':
                    self.goal = self.Node(x, y, None)
                    self.height_map[y][x] = ord('z')
                if char == 'a':
                    self.a_positions.append(self.Node(x, y, None))

    def edges(self, v, explored):
        edges = []
        x, y = v.x, v.y
        value = self.height_map[y][x]
        if not explored[y][x-1] and x-1 >= 0 and self.height_map[y][x-1]-1 <= value:
            edges.append(self.Node(x-1, y, v))
        if x+1 < self.width and not explored[y][x+1] and self.height_map[y][x+1]-1 <= value:
            edges.append(self.Node(x+1, y, v))
        if not explored[y-1][x] and y-1 >= 0 and self.height_map[y-1][x]-1 <= value:
            edges.append(self.Node(x, y-1, v))
        if y+1 < self.height and not explored[y+1][x] and self.height_map[y+1][x]-1 <= value:
            edges.append(self.Node(x, y+1, v))
        return edges

    def breadthFirstSearch(self, root):
        explored = [[False for x in range(0, len(self.height_map[0]))] for y in range(0, len(self.height_map))]
        queue = []
        explored[root.y][root.x] = True
        queue.append(root)
        while queue:
            v = queue[0]
            queue = queue[1:]
            if v.x == self.goal.x and v.y == self.goal.y:
                return v
            for edge in self.edges(v, explored):
                explored[edge.y][edge.x] = True
                queue.append(edge)

    def followPath(self, node, length):
        if node.parent is None:
            return length
        return self.followPath(node.parent, length+1)

    def solvePartOne(self, data):
        self.reset()
        self.parseData(data)
        final_node = self.breadthFirstSearch(self.root)
        return self.followPath(final_node, 0)

    def solvePartTwo(self, data):
        self.reset()
        best_a = 440
        self.parseData(data)
        for a in self.a_positions:
            final_node = self.breadthFirstSearch(a)
            if final_node is not None:
                length = self.followPath(final_node, 0)
                if length < best_a:
                    best_a = length
        return best_a
