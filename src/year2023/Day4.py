import sys
sys.path.append('../../src')

from PythonFramework.Day import Day


class Day4(Day):
    def solvePartOne(self, data):
        cardWins = []
        for line in data:
            mine = [int(x) for x in line.split(': ')[1].split(' | ')[0].split(' ') if x != '']
            winning = [int(x) for x in line.split(': ')[1].split(' | ')[1].split(' ') if x != '']
            cardWins.append(sum([1 for x in mine if x in winning]))
            
        return sum([2**(win-1) for win in cardWins if win > 0])

    def solvePartTwo(self, data):
        cardWins = []
        for line in data:
            mine = [x for x in line.split(': ')[1].split(' | ')[0].split(' ') if x != '']
            winning = [x for x in line.split(': ')[1].split(' | ')[1].split(' ') if x != '']
            cardWins.append(sum([1 for x in mine if x in winning]))

        cardQueue = [i for i in range(len(data))]
        i = 0
        while i < len(cardQueue):
            card = cardQueue[i]
            cardQueue += [j for j in range(card+1, card+1+cardWins[card])]
            i += 1

        return len(cardQueue)


Day4(4).getResult()
