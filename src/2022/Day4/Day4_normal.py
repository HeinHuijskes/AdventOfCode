def getResult():
    data = open('data.txt', 'r').read().split('\n')[:-1]
    print(solvePartOne(data))
    print(solvePartTwo(data))


def solvePartOne(data):
    counter = 0
    for chunk in data:
        # A chunk is represented by 'a-b,x-y'
        range1, range2 = chunk.split(',')
        numbers = range1.split('-')
        a, b = [int(numbers[0]), int(numbers[1])]
        numbers = range2.split('-')
        x, y = [int(numbers[0]), int(numbers[1])]
        # Check to see if either range falls within the other one
        if (a <= x and b >= y) or (a >= x and b <= y):
            counter += 1
    return counter


def solvePartTwo(data):
    counter = 0
    for chunk in data:
        range1, range2 = chunk.split(',')
        numbers = range1.split('-')
        a, b = [int(numbers[0]), int(numbers[1])]
        numbers = range2.split('-')
        x, y = [int(numbers[0]), int(numbers[1])]
        # The only cases of no overlap are when b < x or a > y
        if not (b < x or a > y):
            counter += 1
    return counter


getResult()
