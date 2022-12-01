from src.framework.RetrieveData import getData

data = getData(1, 2022)


def getResult():
    return solve(data)


def solve(data):
    chunks = data.split('\n')

    max_calories = 0
    current_calories = 0
    for chunk in chunks:
        if not chunk.isnumeric():
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
            continue
        current_calories += int(chunk)
    solution = max_calories

    return solution


print(getResult())
