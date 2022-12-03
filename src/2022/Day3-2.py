from src.framework.RetrieveData import getData

data = getData(3, 2022)


def getResult():
    return solve(data)


def solve(data):
    # ADD SOLUTION BELOW
    chunks = data.split('\n')[:-1]
    value = 0
    for i in range(0, len(chunks)):
        if i % 3 != 0:
            continue
        first, second, third = set(chunks[i]), set(chunks[i+1]), set(chunks[i+2])
        char_value = ord(first.intersection(second).intersection(third).pop()) - 96
        if char_value < 0:
            char_value += 58
        value += char_value
    solution = value
    # ADD SOLUTION ABOVE
    return solution


print(getResult())
