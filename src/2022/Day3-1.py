from src.framework.RetrieveData import getData

data = getData(3, 2022)


def getResult():
    return solve(data)


def solve(data):
    # ADD SOLUTION BELOW
    chunks = data.split('\n')[:-1]
    value = 0
    for chunk in chunks:
        length = len(chunk) // 2
        first, second = set([char for char in chunk[length:]]), set([char for char in chunk[:length]])
        char_value = ord(first.intersection(second).pop()) - 96
        if char_value < 0:
            char_value += 58
        value += char_value
    solution = value
    # ADD SOLUTION ABOVE
    return solution


print(getResult())
