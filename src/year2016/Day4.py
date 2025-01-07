import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Solver(Day):
    def parse(self, data):
        parsed = []
        for line in data:
            id, checksum = int(line[-10:-7]), line[-6:-1]
            letters = ''.join(line[:-10].split('-'))
            parsed.append([id, checksum, letters])
        return parsed
    
    def getValidRooms(self, data):
        results = []
        for id, checksum, letters in data:
            frequency = {}
            for letter in letters:
                if letter not in frequency:
                    frequency[letter] = 0
                frequency[letter] += 1

            most_frequent = []
            while len(most_frequent) < 5:
                most = max(frequency.values())
                largest = sorted([letter for letter in frequency if frequency[letter] == most])
                most_frequent += largest
                for letter in largest:
                    frequency.pop(letter)
            correct_checksum = ''.join(most_frequent[:5])
            if checksum == correct_checksum:
                results.append((id, letters))
        return results

    def solvePartOne(self, data):
        self.rooms = self.getValidRooms(data)
        return sum([room[0] for room in self.rooms])

    def solvePartTwo(self, data):
        for id, letters in self.rooms:
            cycles = id % 26
            result = ''
            for letter in letters:
                cycled_letter = ord(letter) + cycles
                if cycled_letter > ord('z'):
                    cycled_letter -= 26
                result += chr(cycled_letter)
            if result == 'northpoleobjectstorage':
                return id


Solver(day=4).getResult(testOnly=False)
