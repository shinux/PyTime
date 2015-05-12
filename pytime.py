#!/usr/bin/env python
# encoding: utf-8

"""
    pytime
    ~~~~~~~~~~~~~

    A easy-use module to solve the common needs of date/time/datetime.

    :copyright: (c) 2015 by Sinux <nsinux@gmail.com>
    :license: MIT, see LICENSE for more details.
"""


import datetime
import calendar
from filter import BaseParser


bp = BaseParser.main


def parse(value):
    return bp(value)


def count(value1, value2):
    return parse(value1) - parse(value2)

# max, min

_date = datetime.date.today()
_year = _date.year
_month = _date.month
_day = _date.day


def today(year=None):
    """this day, last year"""
    return datetime.date(int(year), _date.month, _date.day) if year else _date


def tomorrow(date=None):
    """tomorrow is another day"""
    if not date:
        return _date + datetime.timedelta(days=1)
    else:
        current_date = parse(date)
        return current_date + datetime.timedelta(days=1)


def yesterday(date=None):
    """yesterday once more"""
    if not date:
        return _date - datetime.timedelta(days=1)
    else:
        current_date = parse(date)
        return current_date - datetime.timedelta(days=1)


########################
# Exceptions
########################


class PyTimeException(Exception):
    """ A base class for exceptions used by pytime. """


########################
# function method
########################


def daysrange(start=None, end=None):
    """
    return all days between start and end

    :param start: datetime, date or string
    :param end: datetime, date or string
    :return: list
    """
    days_between = (end - start).days
    date_list = [end - datetime.timedelta(days=x) for x in range(0, days_between+1)]
    return date_list


def lastday(year=_year, month=_month):
    """
    return the current month's last day
    :param year:  default to current year
    :param month:  default to current month
    :return: month's last day
    """
    last_day = calendar.monthrange(year, month)[1]
    return datetime.date(year=year, month=month, day=last_day)


######################
# festival
######################


def newyear(year=None):
    return datetime.date(int(year), 1, 1) if year else datetime.date(_year, 1, 1)


def valentine(year=None):
    return datetime.date(int(year), 2, 14) if year else datetime.date(_year, 2, 14)


def fool(year=None):
    return datetime.date(int(year), 4, 1) if year else datetime.date(_year, 4, 1)


def christmas(year=None):
    return datetime.date(int(year), 12, 25) if year else datetime.date(_year, 12, 25)


def chriseve(year=None):
    return yesterday(christmas(year))


def mother(year=None):
    """
    the 2nd Sunday in May
    :param year: int
    :return: Mother's day
    """
    may_first = datetime.date(_year, 5, 1) if not year else datetime.date(int(year), 5, 1)
    weekday_seq = may_first.weekday()
    return datetime.date(may_first.year, 5, (14 - weekday_seq))


def father(year=None):
    """
    the 3rd Sunday in June
    :param year: int
    :return: Father's day
    """
    june_first = datetime.date(_year, 6, 1) if not year else datetime.date(int(year), 6, 1)
    weekday_seq = june_first.weekday()
    return datetime.date(june_first.year, 6, (21 - weekday_seq))


def halloween(year=None):
    return lastday(month=10) if not year else lastday(year, 10)


def easter(year=None):
    """
    1900 - 2099 limit
    :param year: int
    :return: Easter day
    """
    y = int(year) if year else _year
    n = y - 1900
    a = n % 19
    q = n / 4
    b = (7 * a + 1) / 19
    m = (11 * a + 4 - b) % 29
    w = (n + q + 31 - m) % 7
    d = 25 - m - w
    if d > 0:
        return datetime.date(y, 4, d)
    else:
        return datetime.date(y, 3, (31 - d))


def thanks(year=None):
    """
    4rd Thursday in Nov
    :param year: int
    :return: Thanksgiving Day
    """
    nov_first = datetime.date(_year, 11, 1) if not year else datetime.date(int(year), 11, 1)
    weekday_seq = nov_first.weekday()
    if weekday_seq > 3:
        current_day = 32 - weekday_seq
    else:
        current_day = 25 - weekday_seq
    return datetime.date(nov_first.year, 11, current_day)


if __name__ == '__main__':
    # _time_filter('2015-01-03')
    # print(calendar.monthrange(2015, 10))
    print(bp('2015-01-03'))
