from src.PythonFramework.Misc import *
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

    path = absp + '/../year' + str(year) + '/Day' + str(day) + '/'
    setupStructure(day, year, path)
    makeTests(path)

    for mode in ['']:
        try:
            filename = 'Day' + str(day) + mode + '.py'
            file = open(path + filename, 'x')
            template = open(absp + '/DayTemplate.txt', 'r').read()
            template = template.split('%%')
            day_file = template[0] + str(day) + template[1] + str(day) + template[2]
            file.write(day_file)
        except FileExistsError:
            pass


def setupStructure(day, year, path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

    try:
        if getTimeInHours() < 6:
            print('Data will be made available at 6:00')
            return
        file = open(path + 'data.txt', 'x')
        data = getInputData(day, year)
        file.write(data)
    except FileExistsError:
        pass


def makeTests(path):
    try:
        file = open(path + 'testdata.txt', 'x')
        file.write('')
    except FileExistsError:
        pass


def getInputData(day, year):
    return getData(day, year, addition='/input')


def getData(day, year, addition=''):
    base_url = 'https://adventofcode.com/'
    cookie = {'session': open(absp + '/../common/cookie.txt').readline()}

    r = requests.get(base_url + str(year) + '/day/' + str(day) + addition, cookies=cookie)
    return r.text
