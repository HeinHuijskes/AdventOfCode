from src.framework.Misc import getDate, getAbsolutePath
import requests
import os

absp = getAbsolutePath(__file__)


def setupNewDay():
    day, month, year = getDate()
    setupExactDay(year, month, day)


def setupExactDay(year, month, day):
    if month != 12:
        exit('Wrong month, wait till december')
    elif day > 25:
        exit('Advent of code only lasts until the 25th')

    path = absp + '/../' + str(year) + '/Day' + str(day) + '/'
    setupStructure(day, year, path)

    for mode in ['_normal', '_short']:
        try:
            filename = 'Day' + str(day) + mode + '.py'
            file = open(path + filename, 'x')
            template = open(absp + '/DayTemplate.txt', 'r')
            file.write(template.read())
        except FileExistsError:
            print('A file  for day ' + str(day) + ' already exists, skipping')


def setupStructure(day, year, path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print('Directory already exists, skipped')

    try:
        data = getData(day, year)
        file = open(path + 'data.txt', 'x')
        file.write(data)
    except FileExistsError:
        print('Data already exists, skipped')


def getData(day, year):
    base_url = 'https://adventofcode.com/'
    cookie = {'session': open(absp + '/cookie.txt').readline()}

    r = requests.get(base_url + str(year) + '/day/' + str(day) + '/input', cookies=cookie)
    return r.text
