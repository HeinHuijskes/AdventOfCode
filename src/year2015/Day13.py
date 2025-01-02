import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs


class Day13(Day):
    def parse(self, data):
        people = {}
        for line in data:
            words = line.split(' ')
            person1, sign, amount, person2 = words[0], words[2], int(words[3]), words[10][:-1]
            if sign == 'lose':
                amount = -amount
            if person1 not in people:
                people[person1] = {}
            people[person1][person2] = amount
        return people
    
    def solve(self, data):
        queue = [(0, [person]) for person in data.keys()]
        length = len(queue)
        results = []
        while len(queue) > 0:
            happyiness, people = queue.pop()
            last_person = people[-1]
            if len(people) == length:
                happyiness += data[people[0]][last_person] + data[last_person][people[0]]
                results.append(happyiness)
                continue
            for neighbour in data[last_person]:
                if neighbour not in people:
                    score = data[last_person][neighbour] + data[neighbour][last_person]
                    queue.append((happyiness+score, people+[neighbour]))
        return max(results)

    def solvePartOne(self, data):
        return self.solve(data)

    def solvePartTwo(self, data):
        data['Hein'] = {}
        for person in data:
            if person == 'Hein':
                continue
            data[person]['Hein'] = 0
            data['Hein'][person] = 0
        return self.solve(data)


Day13(13).getResult(testOnly=False)
