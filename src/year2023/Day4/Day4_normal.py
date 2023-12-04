import sys
sys.path.append('../../../src')

from PythonFramework.Day import Day


class Day4(Day):
    def solvePartOne(self, data):
        total = 0
        for line in data:
            points = 0
            mine = [int(x) for x in line.split(': ')[1].split(' | ')[0].split(' ') if x != '']
            winning = [int(x) for x in line.split(': ')[1].split(' | ')[1].split(' ') if x != '']
            # print(mine)
            # print(winning)
            for x in mine:
                if x in winning:
                    points += 1
            if points > 0:
                total += 2 ** (points-1)
            
        return total

    def solvePartTwo(self, data):
        cardQueue = [i+1 for i in range(len(data))]
        i = 1
        while i < len(cardQueue) + 1:
            card = cardQueue[i-1]
            line = data[card-1]
            points = 0
            mine = [int(x) for x in line.split(': ')[1].split(' | ')[0].split(' ') if x != '']
            winning = [int(x) for x in line.split(': ')[1].split(' | ')[1].split(' ') if x != '']
            for x in mine:
                if x in winning:
                    points += 1
            wonCards = [j for j in range(card+1, card+1+points)]
            cardQueue += wonCards
            i += 1

        return len(cardQueue)


Day4().getResult()
