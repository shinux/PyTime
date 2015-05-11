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


def today(year=None):
    """this day, last year"""
    _c_day = datetime.date.today()
    return _c_day if not year else datetime.date(year, _c_day.month, _c_day.day)


def tomorrow(date=None):
    """tomorrow is another day"""
    return datetime.date.today() + datetime.timedelta(days=1)


def yesterday():
    """yesterday once more"""
    return datetime.date.today() - datetime.timedelta(days=1)


# 节日


########################
# Exceptions
########################

class PyTimeException(Exception):
    """ A base class for exceptions used by pytime. """


########################
# Filters
########################


# TODO:move to filter.py
def _time_filter(time, type=None):
    """
    Turn parameter to formatted time type.
    :param time:
    :return: datetime or date
    """
    if isinstance(time, datetime.datetime):
        pass
    elif isinstance(time, datetime.date):
        pass
    elif isinstance(time, str):
        pass


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


def lastday(date, *args, **kwargs):
    """
    return the current month's last day
    :param args:
    :param kwargs:
    :return:
    """
    year = date.year
    month = date.month
    last_day = calendar.monthrange(year, month)[1]

    return datetime.date(year=year, month=month, day=last_day)


if __name__ == '__main__':
    # _time_filter('2015-01-03')
    # print(calendar.monthrange(2015, 10))
    print(bp('2015-01-03'))
