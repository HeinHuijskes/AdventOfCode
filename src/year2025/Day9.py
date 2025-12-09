from src.PythonFramework.Day import Day
import src.PythonFramework.Algorithms as algs


class Solver(Day):
    # Very interesting day given some analysis of the data.
    # Much easier to understand when using visualisation, see self.desmosOutput()
    test_answers = [50, 24]
    answers = [4755064176, 1613305596]

    def parse(self, data: list[str]):
        return [tuple(int(x) for x in r.split(',')) for r in data]

    def solvePartOne(self, data):
        maximum = 0
        self.areas = {}
        for i in range(len(data)-1):
            for j in range(i+1, len(data)):
                (x1, y1), (x2, y2) = data[i], data[j]
                area = (x1-x2+1) * (y1-y2+1)
                if area not in self.areas:
                    self.areas[area] = []
                self.areas[area].append([(x1, y1), (x2, y2)])
                if area > maximum:
                    maximum = area
        return maximum

    def solvePartTwo(self, data):
        # self.desmosOutput(data)
        lines = [(data[i-1],data[i]) for i in range(len(data))]

        # Obtain the starting point
        (upx, upy), (downx, downy) = self.findCut(lines)
        # Ray trace the starting point upwards
        (ax, ay), (bx, by) = self.findNearestIntersect(lines, ((upx,upy+1),(upx,upy+100000)))
        ux, uy = min(ax,bx), ay
        # Ray trace to the left (assumes no obstacles on the left, since then the area would be small)
        (ax, ay), (bx, by) = self.findNearestIntersect(lines, ((ux-1, uy), (ux-100000, uy)))
        lx, ly = ax, min(ay, by)
        # Ray trace down
        (ax, ay), (bx, by) = self.findNearestIntersect(lines, ((lx, ly-1), (lx, ly-100000)))
        dx, dy = max(ax,bx), ay
        # Check whether the trace down ended up at the correct location 
        if (bx, by) == (upx,upy):
            # If so, return the area of the found rectangle
            return (upx - lx + 1) * (ly - upy + 1)
        else:
            # If not, the ray was blocked, so find the line next to the blocker in the cycle, this should contain the correct corner
            # (Assumes maximum of one blockade)
            for (ax, ay), (bx, by) in lines:
                if ax == bx and ((ax, ay) == (dx, dy) or (bx, by) == (dx, dy)):
                    # Adjacent line found
                    rx, ry = ax, max(ay,by)
                    break
            return (upx - rx + 1) * (ry - upy + 1)

    def desmosOutput(self, data):
        # Analyze the data using https://www.desmos.com/calculator/
        with open('testfile.txt', 'a') as f:
            lx, ly = data[-1]
            for nx, ny in data:
                is_x = lx == nx
                if is_x:
                    f.write('x=' + str(nx) + '\\left\\{' + str(max(ny,ly)) + '>y>' + str(min(ny,ly)) + '\\right\\} \n')
                else:
                    f.write('y=' + str(ny) + '\\left\\{' + str(max(nx,lx)) + '>x>' + str(min(nx,lx)) + '\\right\\} \n')
                lx, ly = nx, ny

    def findCut(self, lines):
        # Find the large cut through the circle (see desmosOutput() in a graph for more clarity on the data structure)
        maximi = [0, 0]
        points = [(), ()]
        for (lx, ly), (nx, ny) in lines:
            # Look only for horizontal cuts
            if ny == ly:
                dist = abs(nx-lx)
                # Keep the 2 highest lines, these compose the cut
                if dist > maximi[0]:
                    maximi[1], points[1] = maximi[0], points[0]
                    maximi[0], points[0] = dist, (max(lx,nx), ly)
            lx, ly = nx, ny

        # Return as (upperline, lowerline)
        point1, point2 = points
        if point1[1] > point2[1]:
            return point1, point2
        else:
            return point2, point1
    
    def findNearestIntersect(self, lines, start_line):
        # Find the nearest line that intersects with the start_line
        (aslx, asly), (bslx, bsly) = start_line
        intersect = start_line
        for ((ax, ay), (bx, by)) in lines:
            # Line is vertical
            if aslx == bslx and ay == by:
                # Check intersection
                if min(ax,bx) <= aslx <= max(ax,bx) and min(asly,bsly) <= ay <= max(asly,bsly):
                    # Keep only the closest line
                    if abs(start_line[0][1] - by) < abs(intersect[0][1] - intersect[1][1]):
                        intersect = (((ax, ay), (bx, by)))
            # Line is horizontal
            elif asly == bsly and ax == bx:
                # Check intersection
                if min(ay,by) <= asly <= max(ay,by) and min(aslx,bslx) <= ax <= max(aslx,bslx):
                    # Keep only the closest line
                    if abs(start_line[0][0] - by) < abs(intersect[0][0] - intersect[1][0]):
                        intersect = (((ax, ay), (bx, by)))
        return intersect
        