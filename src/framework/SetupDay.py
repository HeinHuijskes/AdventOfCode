from src.framework.Misc import getDate, getAbsolutePath

absp = getAbsolutePath(__file__)


def setupNewDay():
    day, month, year = getDate()
    setupExactDay(year, month, day)


def setupExactDay(year, month, day):
    if month != 12:
        exit('Wrong month, wait till december')
    elif day > 25:
        exit('Advent of code only lasts until the 25th')

    for i in [1, 2]:
        filename = absp + '/../' + str(year) + '/Day' + str(day) + '-' + str(i) + '.py'
        try:
            file = open(filename, 'x')
            template = open(absp + '/DayTemplate', 'r')
            data = template.read().split('{x}')
            new_data = data[0] + str(day) + data[1] + str(year) + data[2]
            file.write(new_data)
        except FileExistsError:
            print('File ' + str(i) + ' for day ' + str(day) + ' already exists, skipping')
            continue
