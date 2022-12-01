from src.framework.RetrieveData import __getData

data = __getData(0, 2022)


def getResult():
    return solve(data)


def solve(data):
    # ADD SOLUTION BELOW
    chunks = data.split('\n')
    solution = chunks[0]
    # ADD SOLUTION ABOVE
    return solution


print(getResult())
