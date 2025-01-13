from src.PythonFramework.Day import Day


class Day17(Day):
    def parse(self, data):
        A = int(data[0].split(': ')[1])
        B = int(data[1].split(': ')[1])
        C = int(data[2].split(': ')[1])
        program = [int(x) for x in data[4][8:].split(',')]
        self.execute = [self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv]
        return A, B, C, program

    def combo(self, number):
        if number <= 3:
            return number
        elif number == 4:
            return self.A
        elif number == 5:
            return self.B
        elif number == 6:
            return self.C

    def adv(self, operand):
        self.A = int(self.A / 2**self.combo(operand))

    def bxl(self, operand):
        self.B = self.B ^ operand

    def bst(self, operand):
        self.B = self.combo(operand) % 8

    def jnz(self, operand):
        if self.A != 0:
            self.pointer = operand - 2

    def bxc(self, operand):
        self.B = self.C ^ self.B

    def out(self, operand):
        self.output.append(self.combo(operand) % 8)

    def bdv(self, operand):
        self.B = int(self.A / 2**self.combo(operand))

    def cdv(self, operand):
        self.C = int(self.A / 2**self.combo(operand))

    def solvePartOne(self, data):
        A, B, C, program = data
        self.pointer = 0
        self.output = []
        self.A, self.B, self.C = A, B, C
        while self.pointer < len(program):
            opcode, operand = program[self.pointer], program[self.pointer+1]
            self.execute[opcode](operand)
            self.pointer += 2
        return ','.join([str(x) for x in self.output])

    def solvePartTwo(self, data):
        A, B, C, program = data
        queue = [(0, 1)]
        # Depth-first search for the correct A, in reverse order of the content of the program
        while len(queue) > 0:
            number, level = queue.pop()
            A_values = []
            # Only works if the operand for operator 0 (adv) is 3, then A is divided by 8 every loop
            # The next value of the program is found by looking at values A*8 to A*8+8
            for A in range(number, number+8):
                self.pointer = 0
                self.output = []
                self.A, self.B, self.C = A, B, C
                # Just one round of program at a time to find each number in the program separately
                for pointer in range(0, len(program), 2):
                    opcode, operand = program[pointer], program[pointer+1]
                    self.execute[opcode](operand)
                value = self.output[-1]
                if program[-level] == value:
                    if level == len(program):
                        # Found lowest value for A!
                        return A
                    A_values.append(A)
            # Always append the lowest A last, so that it is looked at first
            for A in sorted(A_values, reverse=True):
                queue.append((A*8, level+1))
