from src.framework.RetrieveData import getData

data = getData(2, 2022)


def getResult():
    return solve(data)


def solve(data):
    chunks = data.split('\n')[:-1]
    opt = {'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}
    return sum([(lambda c: opt[c])(c) for c in chunks])


print(getResult())
