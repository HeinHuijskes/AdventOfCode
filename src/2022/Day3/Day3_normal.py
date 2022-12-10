def getResult():
    data = open('data.txt', 'r').read().split('\n')[:-1]
    print(solvePartOne(data))
    print(solvePartTwo(data))


def solvePartOne(data):
    value = 0
    for chunk in data:
        length = len(chunk) // 2
        first, second = set([char for char in chunk[length:]]), set([char for char in chunk[:length]])
        char_value = ord(first.intersection(second).pop()) - 96
        if char_value < 0:
            char_value += 58
        value += char_value
    return value


def solvePartTwo(data):
    value = 0
    for i in range(0, len(data)):
        if i % 3 != 0:
            continue
        first, second, third = set(data[i]), set(data[i+1]), set(data[i+2])
        char_value = ord(first.intersection(second).intersection(third).pop()) - 96
        if char_value < 0:
            char_value += 58
        value += char_value
    return value


getResult()
