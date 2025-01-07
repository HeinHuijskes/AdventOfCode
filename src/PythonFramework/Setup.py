from src.PythonFramework.Misc import *
import requests
import os

absp = getAbsolutePath(__file__)


def setupNewDay():
    day, month, year = getDate()
    setupExactDay(year, day, month)


def setupExactDay(year, day, month=12):
    if month != 12:
        exit('Wrong month, wait till december')
    elif day > 25:
        exit('Advent of code only lasts until the 25th')

    data_path = f'{absp}/../data/year{year}/Day{day}'
    file_path = f'{absp}/../year{year}'
    file_path_day = f'{file_path}/Day{day}.py'
    makeDataFiles(data_path, day, year)

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    if not os.path.exists(file_path_day):
        file = open(f'{file_path_day}', 'x')
        template = open(f'{absp}/DayTemplate.txt', 'r').read()
        template = template.replace('%%', str(day))
        file.write(template)


def makeDataFiles(path, day, year):
    if not os.path.exists(path):
        os.makedirs(path)

    testfile = f'{path}/testdata.txt'
    if not os.path.exists(testfile):
        file = open(testfile, 'x')
        file.write('')
        print(f'Made file: {testfile}')

    datafile = f'{path}/data.txt'
    if not os.path.exists(datafile):
        file = open(datafile, 'x')
        data = getInputData(day, year)
        file.write(data)
        print(f'Made file: {datafile}/data.txt')


def getInputData(day, year):
    return getData(day, year, addition='/input')


def getData(day, year, addition=''):
    base_url = 'https://adventofcode.com/'
    cookie = {'session': open(absp + './cookie.txt').readline()}

    r = requests.get(base_url + str(year) + '/day/' + str(day) + addition, cookies=cookie)
    return r.text


def runDay(day=None, year=None):
    d, m, y = getDate()
    if year == None:
        year = y
    if day == None:
        day = d
    day_path = f'./src/year{year}'
    os.system(f'cd {day_path} && python Day{day}.py')
