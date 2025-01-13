from src.PythonFramework.Day import Day


class Day14(Day):
    def parse(self, data):
        positions, velocities = [], []
        for line in data:
            p, v = line.split(' ')
            positions.append([int(x) for x in p[2:].split(',')])
            velocities.append([int(x) for x in v[2:].split(',')])
        return positions, velocities
    
    def computeQScore(self, positions, dim_x, dim_y):
        half_x, half_y = dim_x // 2, dim_y // 2
        q = [0, 0, 0, 0]
        for i in range(len(positions)):
            (x, y) = positions[i]
            if 0 <= x < half_x:
                if 0 <= y < half_y:
                    q[0] += 1
                elif half_y < y < dim_y:
                    q[2] += 1
            elif half_x < x < dim_x:
                if half_y < y < dim_y:
                    q[3] += 1
                elif 0 <= y < half_y:
                    q[1] += 1
        return q[0] * q[1] * q[2] * q[3]

    def getPositionsAt(self, positions, velocities, dim_x, dim_y, at):
        new_positions = []
        for i in range(len(positions)):
            (x, y), (dx, dy) = positions[i], velocities[i]
            x, y = x + at * dx, y + at * dy
            x, y = x % dim_x, y % dim_y
            new_positions.append((x, y))
        return new_positions

    def solvePartOne(self, data):
        positions, velocities = data
        dim_x, dim_y = 11, 7
        if len(positions) > 12:
            dim_x, dim_y = 101, 103
        new_positions = self.getPositionsAt(positions, velocities, dim_x, dim_y, 100)
        return self.computeQScore(new_positions, dim_x, dim_y)

    def solvePartTwo(self, data):
        positions, velocities = data
        if len(positions) <= 12:
            return 'No test for this one'
        dim_x, dim_y = 101, 103
        lowest_qscore, lowest_i = 100000000000, 0
        for i in range(1, dim_x*dim_y):
            positions = self.getPositionsAt(positions, velocities, dim_x, dim_y, 1)
            qscore = self.computeQScore(positions, dim_x, dim_y)
            if qscore < lowest_qscore:
                lowest_qscore, lowest_i = qscore, i
        return lowest_i
