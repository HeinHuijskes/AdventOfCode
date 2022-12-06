def getResult():
    data = open('data.txt', 'r').read().split('\n')[0]
    print(solvePartOne(data))
    print(solvePartTwo(data))


def solvePartOne(data):
    for i in range(0, len(data)):
        a, b, c, d = data[i], data[i+1], data[i+2], data[i+3]
        if a != b and a != c and a != d and b != c and b != d and c != d:
            return i + 4


def solvePartTwo(data):
    def recursion(chars):
        if len(chars) == 1:
            return True
        else:
            char = chars[0]
            for i in range(1, len(chars)):
                if char == chars[i]:
                    return False
        return recursion(chars[1:])

    for i in range(0, len(data)):
        characters = [data[x] for x in range(i, i+14)]
        if recursion(characters):
            return i + 14


getResult()
