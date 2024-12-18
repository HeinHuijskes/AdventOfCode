import sys
sys.path.append('../../../src')

import time

from PythonFramework.Day import Day
from PythonFramework.Algorithms import *


class Day15(Day):
    def parse(self, data):
        data = '--'.join(data)
        warehouse, moves = data.split('----')
        warehouse, moves = warehouse.split('--'), ''.join(moves.split('--'))
        warehouse = [[char for char in line] for line in warehouse]
        directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
        moves = [directions[move] for move in moves]
        return warehouse, moves
    
    def displayWarehouse(self, warehouse):
        print()
        print('\n'.join([''.join(line) for line in warehouse]))
    
    def hasSpace(self, move, robot, warehouse):
        x, y = robot
        x_dir, y_dir = move
        x_lim, y_lim = len(warehouse[0]), len(warehouse)
        array = []
        while 0 <= x <= x_lim and 0 <= y <= y_lim:
            x, y = x+x_dir, y+y_dir
            if warehouse[y][x] == '.':
                return True, array
            elif warehouse[y][x] == 'O':
                array.append((x, y))
            elif warehouse[y][x] == '#':
                return False, []
    
    def move(self, move, robot, warehouse):
        rx, ry = robot
        x_dir, y_dir = move
        space, boxes = self.hasSpace(move, robot, warehouse)
        if not space:
            return robot
        if len(boxes) > 0:
            (last_x, last_y), (first_x, first_y) = boxes[-1], boxes[0]
            warehouse[last_y+y_dir][last_x+x_dir] = 'O'
        else:
            first_x, first_y = rx+x_dir, ry+y_dir
        warehouse[first_y][first_x] = '@'
        warehouse[ry][rx] = '.'
        return (first_x, first_y)
    
    def hasWideSpace(self, move, robot, warehouse):
        x, y = robot
        x_dir, y_dir = move
        x_lim, y_lim = len(warehouse[0]), len(warehouse)
        array = []
        if x_dir != 0:
            while 0 <= x <= x_lim and 0 <= y <= y_lim:
                x, y = x+x_dir, y+y_dir
                tile = warehouse[y][x]
                if tile == '.':
                    return True, array
                elif tile == '[' or tile == ']':
                    array.append((x, y, tile))
                elif tile == '#':
                    return False, []
        else:
            checkTiles = [(x, y+y_dir)]
            if warehouse[y+y_dir][x] == '[':
                checkTiles.append((x+1, y+y_dir))
            elif warehouse[y+y_dir][x] == ']':
                checkTiles.append((x-1, y+y_dir))
            while len(checkTiles) > 0:
                x, y = checkTiles.pop(0)
                tile = warehouse[y][x]
                if tile == '.':
                    continue
                elif tile == '[':
                    checkTiles.append((x, y+y_dir))
                    checkTiles.append((x+1, y+y_dir))
                    if (x, y, tile) not in array:
                        array.append((x, y, tile))
                    if (x+1, y, ']') not in array:
                        array.append((x+1, y, ']'))
                elif tile == ']':
                    checkTiles.append((x, y+y_dir))
                    checkTiles.append((x-1, y+y_dir))
                    if (x, y, tile) not in array:
                        array.append((x, y, tile))
                    if (x-1, y, '[') not in array:
                        array.append((x-1, y, '['))
                elif tile == '#':
                    return False, []
            return True, array
    
    def moveWide(self, move, robot, warehouse):
        rx, ry = robot
        x_dir, y_dir = move
        space, boxes = self.hasWideSpace(move, robot, warehouse)
        if not space:
            return robot
        for x, y, box in reversed(boxes):
            warehouse[y+y_dir][x+x_dir] = box
            warehouse[y][x] = '.'
        warehouse[ry+y_dir][rx+x_dir] = '@'
        warehouse[ry][rx] = '.'
        return (rx+x_dir, ry+y_dir)

    def solvePartOne(self, data):
        warehouse, moves = data
        robot = [(x, y) for x in range(len(warehouse[0])) for y in range(len(warehouse)) if warehouse[y][x] == '@'][0]
        for move in moves:
            robot = self.move(move, robot, warehouse)
        result = 0
        for y in range(len(warehouse)):
            for x in range(len(warehouse[0])):
                if warehouse[y][x] == 'O':
                    result += y*100 + x
        return result

    def solvePartTwo(self, data):
        warehouse, moves = data
        new_warehouse = []
        for line in warehouse:
            array = []
            for char in line:
                if char == 'O':
                    array += ['[', ']']
                elif char == '@':
                    array += '@.'
                else:
                    array += [char, char]
            new_warehouse.append(array)
        warehouse = new_warehouse
        self.displayWarehouse(warehouse)
        robot = [(x, y) for x in range(len(warehouse[0])) for y in range(len(warehouse)) if warehouse[y][x] == '@'][0]
        for move in moves:
            robot = self.moveWide(move, robot, warehouse)
        result = 0
        self.displayWarehouse(warehouse)
        for y in range(len(warehouse)):
            for x in range(len(warehouse[0])):
                if warehouse[y][x] == '[':
                    result += y*100 + x
        return result


Day15().getResult(testOnly=False)
