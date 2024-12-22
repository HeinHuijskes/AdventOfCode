def getResult():
    data = open('data.txt', 'r').read().split('\n')[:-1]
    print(solvePartOne(data))
    print(solvePartTwo(data))


def solvePartOne(data):
    intersections = []
    for chunk in data:
        set1 = set(chunk[len(chunk) // 2:])
        set2 = set(chunk[:len(chunk) // 2])
        intersect = set1.intersection(set2).pop()
        intersections.append(ord(intersect) - 96)

    result = []
    for intersect in intersections:
        if intersect > 0:
            result.append(intersect)
        else:
            result.append(intersect + 58)

    return sum(result)


def solvePartTwo(data):
    intersections = []
    for i in range(0, len(data)):
        if i % 3 == 0:
            set1 = set(data[i])
            set2 = set(data[i + 1])
            set3 = set(data[i + 2])
            x = set1.intersection(set2, set3).pop()
            intersections.append(ord(x) - 96)

    result = []
    for intersection in intersections:
        if intersection > -1:
            result.append(intersection)
        else:
            result.append(intersection + 58)

    return sum(result)


getResult()
