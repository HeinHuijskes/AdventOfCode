import requests
import src.framework.Misc as Misc

absp = Misc.getAbsolutePath(__file__)


def getData(day, year):
    base_url = 'https://adventofcode.com/'
    cookie = {'session': open(absp + '/cookie').readline()}

    r = requests.get(base_url + str(year) + '/day/' + str(day) + '/input', cookies=cookie)
    return r.text
