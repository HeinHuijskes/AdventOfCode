from src.framework.RetrieveData import getData

data = getData(3, 2022)


def getResult():
    return solve(data.split('\n')[:-1])


def solve(data):
    c = [ord(set(x[len(x)//2:]).intersection(set(x[:len(x)//2])).pop())-96 for x in data]
    return sum([(lambda x: x if x > 0 else x+58)(x) for x in c])


print(getResult())
