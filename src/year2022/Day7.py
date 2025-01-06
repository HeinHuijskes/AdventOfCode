import json
import sys
sys.path.append('../../src')

from PythonFramework.Day import Day


class Solver(Day):
    def handleCommand(self, path, commands):
        # No need to do anything with `$ ls`
        if commands[1] == 'ls':
            return path
        path_name = commands[2]
        # Reset the path to the start by returning an empty path
        if path_name == '/':
            return []
        # Go up one directory by removing the last step from the path
        if path_name == '..':
            return path[:-1]
        # A new directory to go to is specified, add it to the path
        path.append(path_name)
        return path

    def addFile(self, tree, path, size, name):
        directory = tree
        # Follow the path to the correct folder
        for step in path:
            directory = directory[step]
        directory[name] = dict()
        if int(size) > 0:
            # If `size > 0`, then `name` is a file with a size
            directory[name]['size'] = int(size)
            directory[name]['type'] = 'file'
        else:
            # The new file must be a directory
            directory[name]['type'] = 'dir'
        return tree

    def addDirectorySizes(self, directory):
        size = 0
        for file_name in directory:
            # Skip types and sizes, only look at files and directories
            if file_name == 'type' or file_name == 'size':
                continue
            file = directory[file_name]
            if file['type'] == 'dir':
                # Recursively add sizes to all subdirectories and add them to the current directory
                size += self.addDirectorySizes(file)
            else:
                # Add the sizes of files to the current directory
                size += file['size']
        directory['size'] = size
        return size

    def sumDirectorySizes(self, directory):
        size = 0
        for file_name in directory:
            # Skip types and sizes, only look at files and directories
            if file_name == 'type' or file_name == 'size':
                continue
            file = directory[file_name]
            if file['type'] == 'dir':
                # Only get sizes for directories with a size of at most 100000
                if file['size'] <= 100000:
                    size += file['size']
                # Recursively get the sizes of all directories
                size += self.sumDirectorySizes(file)
        return size


    def findSmallestSize(self, directory, minimum, lowest):
        for file_name in directory:
            # Skip types and sizes, only look at files and directories
            if file_name == 'type' or file_name == 'size':
                continue
            file = directory[file_name]
            if file['type'] == 'dir':
                # Find values between the minimum required amount and the lowest correct value so far
                if minimum < file['size'] < lowest:
                    lowest = file['size']
                # Recursively look for possible lower correct values
                lowest = self.findSmallestSize(file, minimum, lowest)
        return lowest

    def parse(self, data):
        tree = dict()
        path = []
        for line in data:
            commands = line.split(' ')
            if commands[0] == '$':
                path = self.handleCommand(path, commands)
            elif commands[0] == 'dir':
                tree = self.addFile(tree, path, 0, commands[1])
            else:
                tree = self.addFile(tree, path, commands[0], commands[1])
        return tree

    def solvePartOne(self, data):
        self.addDirectorySizes(data)
        return self.sumDirectorySizes(data)

    def solvePartTwo(self, data):
        self.addDirectorySizes(data)
        total_size = 70000000
        required_space = 30000000
        system_size = data['size']
        space_needed = required_space - (total_size - system_size)
        return self.findSmallestSize(data, space_needed, system_size)


Solver(day=7).getResult()
