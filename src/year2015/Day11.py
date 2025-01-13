from src.PythonFramework.Day import Day


class Solver(Day):
    cycle = 'abcdefghijklmnopqrstuvwxyz'
    def parse(self, data):
        return data[0]
    
    def meetsRequirements(self, password):
        pairs = set()
        has_straight = False
        for i, letter in enumerate(password):
            if letter == 'i' or letter == 'o' or letter == 'l':
                return False
            if i+1 < len(password):
                if password[i+1] == letter:
                    pairs.add(letter)
            if not has_straight and i+2 < len(password):
                if ord(letter) == ord(password[i+1])-1 == ord(password[i+2])-2:
                    has_straight = True
        return len(pairs) >= 2 and has_straight
    
    def incrementPassword(self, password):
        pointer = len(password)-1
        incremented = False

        for i, letter in enumerate(password):
            if letter == 'i' or letter == 'o' or letter == 'l':
                password[i] = self.cycle[self.cycle.index(letter)+1]
                for j in range(i+1, len(password)):
                    password[j] = self.cycle[0]
                break

        while not incremented and pointer >= 0:
            if password[pointer] == self.cycle[-1]:
                password[pointer] = self.cycle[0]
                pointer -= 1
            else:
                password[pointer] = self.cycle[self.cycle.index(password[pointer])+1]
                incremented = True
        return password

    def solvePartOne(self, data):
        password = [char for char in data]
        while not self.meetsRequirements(password):
            password = self.incrementPassword(password)
        return ''.join(password)

    def solvePartTwo(self, data):
        password = [char for char in self.solvePartOne(data)]
        self.incrementPassword(password)
        while not self.meetsRequirements(password):
            password = self.incrementPassword(password)
        return ''.join(password)
