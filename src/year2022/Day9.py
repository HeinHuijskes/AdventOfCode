from src.PythonFramework.Day import Day


class Solver(Day):
    def parse(self, data):
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

    def trackMoves(self, moves, knots=2):
        tail_visited = {(0, 0): True}
        positions = []
        for i in range(0, knots):
            positions.append((0, 0))
        head = len(positions)-1

        for (x, y) in moves:
            divider = max(abs(x), abs(y))
            for i in range(0, divider):
                positions[head] = ((positions[head][0] + x//divider), (positions[head][1] + y//divider))
                self.moveTail(positions)
                tail_visited[positions[0]] = True

        return len(tail_visited)

    def moveTail(self, positions):
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

    def getCharacter(self, x, y, size, positions, center):
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

    def solvePartOne(self, data):
        return self.trackMoves(data)

    def solvePartTwo(self, data):
        return self.trackMoves(data, knots=10)
