word = '_HEIN_'
path = ''


def getStrings(name):
    files = []
    for letter in name:
        file_name = path + 'Letters/' + letter + '.txt'
        files.append(open(file_name, 'r').read().split('\n'))
    return [''.join(line) for line in list(zip(*files))]


def getCorrectSpritePosition(x):
    # Find a correct position for the sprite based on the position of a pixel
    pass


def getRandomSpritePosition(i):
    pass


def addCommand(position, sprite_position, output):
    # This is a tad harder than expected, since it takes two cycles to change the registry, requiring preciser placement
    pass


def getOutput(data):
    output = []
    sprite_position = 1
    for line in data:
        for i in range(0, len(line)):
            position = 1
            if line[i] == '#':
                position = getCorrectSpritePosition(i)
            else:
                position = getRandomSpritePosition(i)
            sprite_position = addCommand(position, sprite_position, output)


def writeToFile(output):
    file_name = path + 'Output/' + word + '.txt'
    file = open(file_name, 'w')
    file.write(output)


def run():
    strings = getStrings(word)
    output = ''
    writeToFile(output)


run()
