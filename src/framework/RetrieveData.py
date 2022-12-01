import requests


def __getData(day, year):
    base_url = 'https://adventofcode.com/'
    cookie = {'session': open('cookie').readline()}

    r = requests.get(base_url + str(year) + '/day/' + str(day) + '/input', cookies=cookie)
    return r.text
