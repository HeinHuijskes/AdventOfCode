from src.PythonFramework.Day import Day

import numpy as np


class Solver(Day):
    def getHandType(self, hand, joker = False):
        a, b, c, d, e = sorted(hand)
        handset_length = len(set(hand))
        hand_type = 100
        if handset_length == 1:
            # 5 of a kind!
            hand_type = 0
        elif handset_length == 2:
            # 4 of a kind or full house
            if a == b and d == e:
                # Full house
                hand_type = 2
            else:
                # 4 of a kind
                hand_type = 1
        elif handset_length == 3:
            # Three of a kind or two pair
            if (a == b and b == c) or (b == c and c == d) or (c == d and d == e):
                # Three of a kind
                hand_type = 3
            else:
                # Two pair
                hand_type = 4
        elif handset_length == 4:
            # One pair
            hand_type = 5
        else:
            # High card
            hand_type = 6
        if joker and 'J' in hand:
            hand_type = self.upgrade(hand, hand_type)
        return hand_type

    def upgrade(self, hand, hand_type):
        # Interestingly, there are a very limited amount of upgrades possible
        # E.g. if the hand type is 'hc', this always means the upgrade is 2p (since the hand is 'Jwxyz')
        # This is based on the assumption that there is at least 1 'J' in the hand to be upgraded
        if hand_type <= 2:
            # 5k, 4k, and fh all get upgraded to 5k
            return 0
        elif hand_type == 3:
            # 3k and 2p both get upgraded to 4k
            return 1
        elif hand_type == 4:
            if sum(['J' == x for x in hand]) == 2:
                # Can upgrade to 4k
                return 1
            else:
                # Can only upgrade to fh
                return 2

        elif hand_type == 5:
            # 1p gets upgraded to 3k
            return 3
        else:
            # hc gets upgraded to 1p
            return 5

    def transformHand(self, hand, joker = False):
        result = 0
        charDict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
        if joker:
            charDict['J'] = 1
        for i, char in enumerate(hand):
            if char.isnumeric():
                result += int(char)*(10**(8-i*2))
            else:
                result += charDict[char]*(10**(8-i*2))
        return result

    def solvePartOne(self, data):
        # Sorting time
        # First divide all hands based on their type
        types = [[], [], [], [], [], [], []]
        # hand_types = ['5k', '4k', 'fh', '3k', '2p', '1p', 'hc']
        for line in data:
            hand, bid = line.split(' ')
            transformed_hand = self.transformHand(hand)
            hand_type = self.getHandType(hand)
            types[hand_type].append([int(transformed_hand), int(bid)])
        result = []
        for t in types:
            if len(t) == 0:
                continue
            np_array = np.array(t)
            id_array = np.argsort(np_array[:, 0])
            sorted_list = [t[id][1] for id in reversed(id_array)]
            result += sorted_list
        return sum([x*(i+1) for i, x in enumerate(reversed(result))])

    def solvePartTwo(self, data):
        types = [[], [], [], [], [], [], []]
        # hand_types = ['5k', '4k', 'fh', '3k', '2p', '1p', 'hc']
        for line in data:
            hand, bid = line.split(' ')
            transformed_hand = self.transformHand(hand, joker = True)
            hand_type = self.getHandType(hand, joker = True)
            types[hand_type].append([int(transformed_hand), int(bid)])
        result = []
        for t in types:
            if len(t) == 0:
                continue
            np_array = np.array(t)
            id_array = np.argsort(np_array[:, 0])
            sorted_list = [t[id][1] for id in reversed(id_array)]
            result += sorted_list
        return sum([x*(i+1) for i, x in enumerate(reversed(result))])
