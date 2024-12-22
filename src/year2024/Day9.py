import sys
sys.path.append('../../src')

from PythonFramework.Day import Day
from PythonFramework.Algorithms import *


class Day9(Day):
    def parse(self, data):
        array = list(map(int, data[0]))
        parsed_array = []
        id = 0
        for i, val in enumerate(array):
            if i % 2 == 0:
                for j in range(val):
                    parsed_array.append(id)
                id += 1
            else:
                for j in range(val):
                    parsed_array.append(-1)
        return parsed_array

    def showString(self, array):
        print(''.join([f'{nr}' if nr != -1 else '.' for nr in array ]))

    def solvePartOne(self, data):
        # self.showString(data)

        empty_count = sum([x == -1 for x in data])
        empty_pointer, data_pointer = -1, len(data)
        empty_index, data_index = None, None

        # Loop while there are still empty points to the left of data entries
        while True:
            # Loop until a new empty point is found
            while not empty_index:
                empty_pointer += 1
                if data[empty_pointer] == -1:
                    empty_index = empty_pointer
            # Break out of the loop when no data is left to move
            if empty_pointer >= len(data) - empty_count:
                break
            # Loop until a new data point is found
            while not data_index:
                data_pointer -= 1
                if data[data_pointer] != -1:
                    data_index = data_pointer
            # Swap data and empty point
            data[empty_pointer] = data[data_pointer]
            data[data_pointer] = -1
            empty_index, data_index = None, None

        # self.showString(data)
        return sum([i*x for i, x in enumerate(data) if x != -1])

    def solvePartTwo(self, data):
        # self.showString(data)

        data_tried = []
        empty_count = sum([x == -1 for x in data])
        empty_pointer, data_pointer = -1, len(data)
        empty_index_start, empty_index_end = None, None
        data_index_start, data_index_end = None, None
        data_length = 0

        # Loop while there are still empty points to the left of data entries
        while True:
            # Loop until a new data point is found
            while not data_index_start:
                data_pointer -= 1
                if data_pointer < 0:
                    break
                if data[data_pointer] != -1 and data[data_pointer] not in data_tried:
                    data_index_end = data_pointer
                    i = data_index_end
                    data_id = data[i]
                    while data[i] == data_id:
                        i -= 1
                    data_index_start = i+1
                    data_length = data_index_end - data_index_start + 1

            # Loop until a new empty point is found
            while not empty_index_start:
                empty_pointer += 1

                # Break out of the loop if the data can't be moved left
                if empty_pointer > data_pointer:
                    data_tried.append(data_id)
                    empty_pointer = -1
                    empty_index_start, empty_index_end = None, None
                    data_index_start, data_index_end = None, None
                    break

                if data[empty_pointer] == -1:
                    empty_index_start = empty_pointer
                    i = empty_index_start
                    while data[i] == -1:
                        i += 1
                    empty_index_end = i-1
                    empty_length = empty_index_end - empty_index_start + 1

                    if empty_length >= data_length:
                        data_tried.append(data_id)
                        # Swap
                        for i in range(data_length):
                            data[empty_index_start+i] = data[data_index_start+i]
                            data[data_index_start+i] = -1
                        # Reset
                        empty_pointer = -1
                        empty_index_start, empty_index_end = None, None
                        data_index_start, data_index_end = None, None
                        # self.showString(data)
                        break
                        
                    else:
                        # Find next empty space
                        empty_pointer = empty_index_end + 1
                        empty_index_start, empty_index_end = None, None

            # Break out of the loop when no data is left to move
            if data_pointer < 0:
                break

        # self.showString(data)
        return sum([i*x for i, x in enumerate(data) if x != -1])


Day9(9).getResult(testOnly=False)
