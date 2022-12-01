from datetime import datetime
import os


def getDate():
    now = datetime.now().date()
    year = now.year
    month = now.month
    day = now.day
    return day, month, year


def getAbsolutePath(file):
    return os.path.dirname(file)
