import functools
import math
import pathlib
from time import time


def parse(puzzle_input):
    values = puzzle_input.split("\n")
    springs = []
    condition = []
    for value in values:
        value = value.split(" ")
        springs.append(value[0])
        cond = []
        for val in value[1].split(","):
            cond.append(int(val))
        condition.append(cond)
    return springs, condition


def count_matches(spring, spr_size, crit):
    if len(crit) == 0:
        # criteria is good, check if there are no more #s
        if not any(value == '#' for value in spring):
            return 1
        else:
            return 0
    # get first criteria and the other stuff
    head = crit[0]
    tail = crit[1:]
    space_needed = sum(tail) + len(tail)
    result = 0
    for before in range(spr_size-space_needed-head+1):
        cand = '.' * before + '#' * head + '.'
        zipped = zip(spring, cand)
        can_do = True
        for c0, c1 in zipped:
            if not (c0 == c1 or c0=='?'):
                can_do = False
                break
        if can_do:
            result += count_matches(spring[len(cand):], spr_size-head-before-1, tail)
    return result


def part1(springs, condition):
    result = 0
    for i in range(len(springs)):
        spring, cond = springs[i], condition[i]
        amount = count_matches(spring, len(spring), cond)
        print(amount)
        result += amount
    return result


def unfold(spring, cond):
    cond = cond * 5
    spring_result = spring
    for i in range(4):
        spring_result = spring_result + '?' + spring
    return spring_result, cond


def part2(springs, condition):
    result = 0
    for i in range(len(springs)):
        spring, cond = unfold(springs[i], condition[i])
        result += count_matches(spring, len(spring), cond)
    return result


def solve(puzzle_input):
    springs, condition = parse(puzzle_input)
    sol1 = part1(springs, condition)
    sol2 = 'part2(springs, condition)'
    return sol1, sol2


def run():
    start_time = time()
    puzzle_input = pathlib.Path("data.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print(solutions)
    print("This took ", time() - start_time)

run()