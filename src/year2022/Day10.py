import sys
sys.path.append('../../src')

from PythonFramework.Day import Day


class Solver(Day):
    cycle = 1
    register = 1
    result = []

    def solvePartOne(self, data):
        self.cycle = 1
        self.register = 1
        self.result = []
        for line in data:
            self.doCycle(False)
            if 'noop' not in line:
                self.doCycle(False)
                self.register += int(line.split(' ')[1])
        print(self.result)
        return sum(self.result)

    def solvePartTwo(self, data):
        self.register = 1
        self.cycle = 1
        self.result = []
        for line in data:
            self.doCycle(True)
            if 'noop' not in line:
                self.doCycle(True)
                self.register += int(line.split(' ')[1])
        return self.draw()

    def doCycle(self, is_part2):
        if is_part2:
            pixel = ' '
            if (self.register - 1) <= ((self.cycle - 1) % 40) <= (self.register + 1):
                pixel = '#'
            self.result.append(pixel)
        elif self.cycle % 40 == 20:
            self.result.append(self.register * self.cycle)
        self.cycle += 1

    def draw(self):
        screen = ''
        height, width = 6, 40
        for h in range(0, height):
            screen += '\n'
            for w in range(0, width):
                screen += self.result[h * width + w]
        print(screen)
        return ''


Solver(day=10).getResult()
