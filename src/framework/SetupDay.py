from datetime import datetime
import os

absp = os.path.dirname(__file__)


def __setupNewDay():
    now = datetime.now().date()
    year = now.year
    month = now.month
    day = now.day
    __setupExactDay(year, month, day)


def __setupExactDay(year, month, day):
    if month != 12:
        exit('Wrong month, wait till december')
    elif day > 25:
        exit('Advent of code only lasts until the 25th')

    for i in [1, 2]:
        filename = absp + '/../../src/' + str(year) + '/Day' + str(day) + '-' + str(i) + '.py'
        try:
            file = open(filename, 'x')
            template = open(absp + '/DayTemplate.py', 'r')
            data = template.read().split('"{{x}}"')
            new_data = data[0] + str(day) + data[1] + str(year) + data[2]
            file.write(new_data)
        except FileExistsError:
            print('File ' + str(i) + ' for day ' + str(day) + ' already exists, skipping')
            continue
