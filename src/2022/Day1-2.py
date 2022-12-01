from src.framework.RetrieveData import getData

data = getData(1, 2022)


def getResult():
    return solve(data)


def solve(data):
    chunks = data.split('\n')

    calories = []
    current_calories = 0
    for chunk in chunks:
        if not chunk.isnumeric():
            calories.append(current_calories)
            current_calories = 0
            continue
        current_calories += int(chunk)
    calories.sort()
    solution = calories[-1] + calories[-2] + calories[-3]

    return solution


print(getResult())
