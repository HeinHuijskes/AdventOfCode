import sys
sys.path.append('src')
from PythonFramework.Day import Day
sys.path.append('src/year2023/Day12')


def reduceSprings(springs):
    result = []
    while len(springs) > 0:
        if springs[0] == '.':
            springs = springs[1:]
            continue
        else:
            array = []
            for x in springs:
                if x == '.':
                    break
                array.append(x == '#')
            result.append(array)
            springs = springs[len(array):]
    return result


def getSubSpring(spring, i, j, number, springs, numbers, path):
    amount = 0
    sub_springs = springs[i+1:]
    # If there are no subsprings left
    if j+number == len(spring):
        path += [(number, spring)]
        amount = recurseSprings(sub_springs, numbers, path)
    # Check that there is no immediate definite spring after this option
    elif (not spring[j+number]):
        # Prepend any large enough leftovers to the springset
        if len(spring) - number - j > 1:
            sub_springs = [spring[number+j+1:]] + sub_springs
        path += [(number, spring[:number+j])]
        amount = recurseSprings(sub_springs, numbers, path)
    return amount

def recurseSprings(springs, numbers, path):
    print(springs, numbers)
    if len(numbers) == 0:
        # Check that there are either no springs left, or only '?' strings (denoted as False)
        if len(springs) == 0 or sum([sum(x) for x in springs]) == 0:
            print('success', path)
            return 1
        else:
            print('failure', path)
            return 0

    # Prune based on options left compared to numbers left.
    if sum(numbers) > sum([len(x) for x in springs]):
        return 0

    number = numbers[0]
    numbers = numbers[1:]
    options = 0
    for i, spring in enumerate(springs):
        if len(spring) == number:
            path += [(number, spring)]
            amount = recurseSprings(springs[i+1:], numbers, path)
            if amount == 0:
                # Pruned
                break
            options += amount
        elif len(spring) > number:
            # Loop over all possible sub_springs
            for j, x in enumerate(spring[:len(spring)-number+1]):
                amount = getSubSpring(spring, i, j, number, springs, numbers, path)
                options += amount
                # If there is a definite spring here, look no further
                if x:
                    break
    return options


class Day12(Day):
    def solvePartOne(self, data):
        total = 0
        for line in data[0:1]:
            notations = line.split(' ')
            springs, numbers = reduceSprings(notations[0]), [int(x) for x in notations[1].split(',')]
            amount = recurseSprings(springs, numbers, [])
            print(f'{amount}')
            total += amount

        return total

    def solvePartTwo(self, data):
        return 'No part 2 solution yet'


Day12(12).getResult(testOnly=False)
