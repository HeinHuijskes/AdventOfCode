import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
import PythonFramework.Algorithms as algs

from regex import regex as re
from math import prod


class Day15(Day):
    def parse(self, data):
        mapping = {}
        for line in data:
            ingredient, cap, d, f, t, cal = re.match(
                '(\w*): \w* (-?\d*), \w* (-?\d*), \w* (-?\d*), \w* (-?\d*), \w* (-?\d*)', line).groups()
            mapping[ingredient] = [int(cap), int(d), int(f), int(t), int(cal)]
        return mapping
    
    def solve(self, data, part2=False): 
        highest = 0
        ingredients = list(data.keys())
        # Initialize 0-100 teaspoons for the first ingredient
        queue = [[[i, ingredients[0]]] for i in range(101)]
        while len(queue) > 0:
            recipe = queue.pop()
            if len(recipe) == len(ingredients):
                # Check that the calories sum to 500 for part 2
                if part2 and not sum([data[ingredient][-1]*number for number, ingredient in recipe]) == 500:
                    continue
                # Calculate the score of the ingredients
                score = prod([max(sum([data[ingredient][i]*number for number, ingredient in recipe]),0) for i in range(len(data[ingredients[0]])-1)])
                highest = max(score, highest)
            else:
                # Cap the amount so that no more than 100 teaspoons are used in total
                amount = sum([ingredient[0] for ingredient in recipe])
                # Find the next ingredient to use
                index = ingredients.index(recipe[-1][1])+1
                if index == len(ingredients)-1:
                    # Only include final recipes that not sum to 100 teaspoons exactly
                    queue.append(recipe + [[100-amount, ingredients[index]]])
                else:
                    for i in range(amount, 101):
                        queue.append(recipe + [[100-i, ingredients[index]]])
        return highest

    def solvePartOne(self, data):
        return self.solve(data)

    def solvePartTwo(self, data):
        return self.solve(data, part2=True)


Day15(15).getResult(testOnly=False)
