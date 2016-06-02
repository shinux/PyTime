#!/usr/bin/env python
# encoding: utf-8

"""
    pytime
    ~~~~~~~~~~~~~

    A easy-use module to solve the datetime needs by string.

    :copyright: (c) 2015 by Sinux <nsinux@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

import datetime
import calendar
from .filter import BaseParser


bp = BaseParser.main
dp = BaseParser.parse_diff


def parse(value):
    return bp(value)


def count(value1, value2):
    _val1, _val2 = parse(value1), parse(value2)
    if type(_val1) == type(_val2):
        return _val1 - _val2
    else:
        _val1 = _val1 if isinstance(_val1, datetime.datetime) else midnight(_val1)
        _val2 = _val2 if isinstance(_val2, datetime.datetime) else midnight(_val2)
        return _val1 - _val2


# max, min


_date = datetime.date.today()
_datetime = datetime.datetime.now()
_year = _date.year
_month = _date.month
_day = _date.day

_SEVEN_DAYS = datetime.timedelta(days=7)
_ONE_DAY = datetime.timedelta(days=1)


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
# function method
########################


def daysrange(first=None, second=None, wipe=False):
    """
    get all days between first and second

    :param first: datetime, date or string
    :param second: datetime, date or string
    :return: list
    """
    _first, _second = parse(first), parse(second)
    (_start, _end) = (_second, _first) if _first > _second else (_first, _second)
    days_between = (_end - _start).days
    date_list = [_end - datetime.timedelta(days=x) for x in range(0, days_between + 1)]
    if wipe and len(date_list) >= 2:
        date_list = date_list[1:-1]
    return date_list


def lastday(year=_year, month=_month):
    """
    get the current month's last day
    :param year:  default to current year
    :param month:  default to current month
    :return: month's last day
    """
    last_day = calendar.monthrange(year, month)[1]
    return datetime.date(year=year, month=month, day=last_day)


def midnight(arg=None):
    """
    convert date to datetime as midnight or get current day's midnight
    :param arg: string or date/datetime
    :return: datetime at 00:00:00
    """
    if arg:
        _arg = parse(arg)
        if isinstance(_arg, datetime.date):
            return datetime.datetime.combine(_arg, datetime.datetime.min.time())
        elif isinstance(_arg, datetime.datetime):
            return datetime.datetime.combine(_arg.date(), datetime.datetime.min.time())
    else:
        return datetime.datetime.combine(_date, datetime.datetime.min.time())


def before(base=_datetime, diff=None):
    """
    count datetime before `base` time
    :param base:  minuend -> str/datetime/date
    :param diff:  str
    :return: datetime
    """
    _base = parse(base)
    if isinstance(_base, datetime.date):
        _base = midnight(_base)
    if not diff:
        return _base
    result_dict = dp(diff)
    # weeks already convert to days in diff_parse function(dp)
    for unit in result_dict:
        _val = result_dict[unit]
        if not _val:
            continue
        if unit == 'years':
            _base = _base.replace(year=(_base.year - _val))
        elif unit == 'months':
            if _base.month <= _val:
                _month_diff = 12 - (_val - _base.month)
                _base = _base.replace(year=_base.year - 1).replace(month=_month_diff)
            else:
                _base = _base.replace(month=_base.month - _val)
        elif unit in ['days', 'hours', 'minutes', 'seconds']:
            _base = _base - datetime.timedelta(**{unit: _val})
    return _base


def after(base=_datetime, diff=None):
    """
    count datetime after diff args
    :param base: str/datetime/date
    :param diff: str
    :return: datetime
    """
    _base = parse(base)
    if isinstance(_base, datetime.date):
        _base = midnight(_base)
    result_dict = dp(diff)
    for unit in result_dict:
        _val = result_dict[unit]
        if not _val:
            continue
        if unit == 'years':
            _base = _base.replace(year=(_base.year + _val))
        elif unit == 'months':
            if _base.month + _val <= 12:
                _base = _base.replace(month=_base.month + _val)
            else:
                _month_diff = (_base.month + _val) - 12
                _base = _base.replace(year=_base.year + 1).replace(month=_month_diff)
        elif unit in ['days', 'hours', 'minutes', 'seconds']:
            _base = _base + datetime.timedelta(**{unit: _val})
    return _base


def _datetime_to_date(arg):
    """
    convert datetime/str to date
    :param arg:
    :return:
    """
    _arg = parse(arg)
    if isinstance(_arg, datetime.datetime):
        _arg = _arg.date()
    return _arg


# Monday to Monday -> 00:00:00 to 00:00:00   month 1st -  next month 1st
def this_week(arg=_date, clean=False):
    _arg = _datetime_to_date(arg)
    return _arg - datetime.timedelta(days=_arg.weekday()), _arg + datetime.timedelta(
        days=6 - _arg.weekday()) if clean else _arg + datetime.timedelta(days=6 - _arg.weekday()) + _ONE_DAY


def last_week(arg=_date, clean=False):
    this_week_tuple = this_week(arg)
    return this_week_tuple[0] - _SEVEN_DAYS, this_week_tuple[1] - _SEVEN_DAYS if clean \
        else this_week_tuple[1] - _SEVEN_DAYS + _ONE_DAY


def next_week(arg=_date, clean=False):
    this_week_tuple = this_week(arg)
    return this_week_tuple[0] + _SEVEN_DAYS, this_week_tuple[1] + _SEVEN_DAYS if clean \
        else this_week_tuple[1] + _SEVEN_DAYS + _ONE_DAY


def this_month(arg=_date, clean=False):
    _arg = _datetime_to_date(arg)
    return datetime.date(_arg.year, _arg.month, 1), lastday(_arg.year, _arg.month) if clean \
        else lastday(_arg.year, _arg.month) + _ONE_DAY


def last_month(arg=_date, clean=False):
    _arg = _datetime_to_date(arg)
    this_month_first_day = datetime.date(_arg.year, _arg.month, 1)
    last_month_last_day = this_month_first_day - _ONE_DAY
    last_month_first_day = datetime.date(last_month_last_day.year, last_month_last_day.month, 1)
    return last_month_first_day, last_month_last_day if clean else this_month_first_day


def next_month(arg=_date, clean=False):
    _arg = _datetime_to_date(arg)
    this_month_last_day = lastday(_arg.year, _arg.month)
    next_month_first_day = this_month_last_day + _ONE_DAY
    next_month_last_day = lastday(next_month_first_day.year, next_month_first_day.month)
    return next_month_first_day, next_month_last_day if clean else next_month_last_day + _ONE_DAY


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


def christeve(year=None):
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
    q = n // 4
    b = (7 * a + 1) // 19
    m = (11 * a + 4 - b) % 29
    w = (n + q + 31 - m) % 7
    d = 25 - m - w
    if d > 0:
        return datetime.date(y, 4, d)
    else:
        return datetime.date(y, 3, (31 + d))


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
