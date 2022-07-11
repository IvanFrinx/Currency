import datetime


def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def yesterday():
    return datetime.date.today() - datetime.timedelta(days=1)
