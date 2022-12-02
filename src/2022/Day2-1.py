from src.framework.RetrieveData import getData

data = getData(2, 2022)


def getResult():
    return solve(data)


def solve(data):
    chunks = data.split('\n')
    # Truncate the end, since it contains an empty string
    chunks = chunks[:-1]
    options = {'A X': 3+1, 'A Y': 6+2, 'A Z': 0+3,
               'B X': 0+1, 'B Y': 3+2, 'B Z': 6+3,
               'C X': 6+1, 'C Y': 0+2, 'C Z': 3+3}

    score = 0
    for chunk in chunks:
        score += options[chunk]
    solution = score
    return solution


print(getResult())
