import json


def getResult():
    test_data = open('testdata.txt', 'r').read()
    if len(test_data) > 0:
        test_data = test_data.split('\n')[:-1]
        print('Test answer part 1:', solvePartOne(test_data))
        print('Test answer part 2:', solvePartTwo(test_data))

    data = open('data.txt', 'r').read().split('\n')[:-1]
    print('Answer part 1:', solvePartOne(data))
    print('Answer part 2:', solvePartTwo(data))


def handleCommand(path, commands):
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


def addFile(tree, path, size, name):
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


def parseData(data):
    tree = dict()
    path = []

    for line in data:
        commands = line.split(' ')

        if commands[0] == '$':
            path = handleCommand(path, commands)

        elif commands[0] == 'dir':
            tree = addFile(tree, path, 0, commands[1])

        else:
            tree = addFile(tree, path, commands[0], commands[1])

    return tree


def addDirectorySizes(directory):
    size = 0
    for file_name in directory:
        # Skip types and sizes, only look at files and directories
        if file_name == 'type' or file_name == 'size':
            continue

        file = directory[file_name]
        if file['type'] == 'dir':
            # Recursively add sizes to all subdirectories and add them to the current directory
            size += addDirectorySizes(file)

        else:
            # Add the sizes of files to the current directory
            size += file['size']

    directory['size'] = size

    return size


def sumDirectorySizes(directory):
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
            size += sumDirectorySizes(file)

    return size


def findSmallestSize(directory, minimum, lowest):
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
            lowest = findSmallestSize(file, minimum, lowest)

    return lowest


def solvePartOne(data):
    tree = parseData(data)
    addDirectorySizes(tree)

    # Write the data to a json file for clearer overview and debugging
    file = open('json_tree.json', 'w')
    file.write(json.dumps(tree, indent=2))

    return sumDirectorySizes(tree)


def solvePartTwo(data):
    tree = parseData(data)
    addDirectorySizes(tree)

    total_size = 70000000
    required_space = 30000000
    system_size = tree['size']
    space_needed = required_space - (total_size - system_size)

    return findSmallestSize(tree, space_needed, system_size)


getResult()
