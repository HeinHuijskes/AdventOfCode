from src.framework.RetrieveData import getData

data = getData(3, 2022)


def getResult():
    return solve(data.split('\n')[:-1])


def solve(d):
    f = lambda i: ord(set(d[i]).intersection(set(d[i + 1])).intersection(set(d[i + 2])).pop()) - 96 if i % 3 == 0 else 0
    return sum([(lambda x: x if x > -1 else x + 58)(x) for x in [f(i) for i in range(0, len(d))]])


print(getResult())
