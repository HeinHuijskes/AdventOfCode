from src.PythonFramework.Misc import getDate, getAbsolutePath
import os

absp = getAbsolutePath(__file__)
print(__file__, absp)


def testToday():
    day, month, year = getDate()
    filename = absp + '/../' + str(year) + '/Day' + str(day) + '-'
    appendage = '.py'
    print(filename)
    for i in [1, 2]:
        print(os.system(filename + str(i) + appendage))


testToday()
