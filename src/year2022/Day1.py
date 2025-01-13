from src.PythonFramework.Day import Day

class Solver(Day):
    def solvePartOne(self, data):
        chunks = data

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

    def solvePartTwo(self, data):
        chunks = data

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
