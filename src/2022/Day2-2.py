from src.framework.RetrieveData import getData

data = getData(2, 2022)


def getResult():
    return solve(data)


def solve(data):
    chunks = data.split('\n')
    # Truncate the end, since it contains an empty string
    chunks = chunks[:-1]
    options = {'A X': 3+0, 'A Y': 1+3, 'A Z': 2+6,
               'B X': 1+0, 'B Y': 2+3, 'B Z': 3+6,
               'C X': 2+0, 'C Y': 3+3, 'C Z': 1+6}

    score = 0
    for chunk in chunks:
        score += options[chunk]
    solution = score
    return solution


print(getResult())
