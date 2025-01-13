import sys
sys.path.append('../../src')

from functools import reduce

from PythonFramework.Day import Day


class Solver(Day):
    def transpose(self, array):
        result = [[y for y in range(len(array))] for x in range(len(array[0]))]
        for x, row in enumerate(array):
            for y, col in enumerate(row):
                result[y][x] = col
        return result

    def expaaaaaand(self, stars):
        for i in range(0,2):
            result = []
            for row in stars:
                result.append(row)
                if sum(row) == 0:
                    result.append(row)
            stars = self.transpose(result)
        return stars

    def displayStars(self, stars):
        for row in stars:
            line = ''
            for col in row:
                if col:
                    line += '#'
                else:
                    line += '.'
            print(line)
        print()

    def getEmpties(self, stars, cols=False):
        if cols:
            stars = self.transpose(stars)
        result = []
        for i, row in enumerate(stars):
            if sum(row) == 0:
                result.append(i)
        return result

    def solvePartOne(self, data):
        stars = [[x == '#' for x in line] for line in data]
        stars = self.expaaaaaand(stars)
        star_duos = list(reduce(lambda a,b: a+b, [x for x in [[(x,y) for x, star in enumerate(row) if star] for y, row in enumerate(stars)] if x != []], []))
        star_duos = [[a, b] for b in star_duos for a in star_duos if a != b]
        star_duos = [abs(ax-bx)+abs(ay-by) for [(ax,ay),(bx,by)] in star_duos]
        return sum(star_duos) // 2

    def solvePartTwo(self, data):
        factor = 1000000
        stars = [[x == '#' for x in line] for line in data]
        empty_rows = self.getEmpties(stars)
        empty_cols = self.getEmpties(stars, cols=True)
        star_coords = list(reduce(lambda a,b: a+b, [x for x in [[(x,y) for x, star in enumerate(row) if star] for y, row in enumerate(stars)] if x != []], []))
        star_duos = []
        for i in range(len(star_coords)):
            for j in range(i, len(star_coords)):
                if i != j:
                    star_duos.append([(star_coords[i]),(star_coords[j])])

        result = []
        for [(ax,ay),(bx,by)] in star_duos:
            rows, cols = 0, 0
            for row in empty_rows:
                if ay < row < by or by < row < ay:
                    rows += 1
            for col in empty_cols:
                if ax < col < bx or bx < col < ax:
                    cols += 1
            result.append(abs(ax-bx)-cols+cols*factor+abs(ay-by)-rows+rows*factor)

        return sum(result)
