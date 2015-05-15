# PyTime
[![Build Status](https://travis-ci.org/shnode/PyTime.svg?branch=master)](https://travis-ci.org/shnode/PyTime) [![Coverage Status](https://coveralls.io/repos/shnode/PyTime/badge.svg)](https://coveralls.io/r/shnode/PyTime)
====

PyTime is a easy-use Python module to solve the common needs of date/time/datetime.

PyTime allows you using string to operate datetime at most situation.

PyTime also provide some simple useful method.

PyTime is a timesaver for Pythonista.

## Install

    pip install pytime

## Simple Usage

calculate `datetime` all by string, accept unit for short or overall length, and they can be out of order or in capital:

    >>>from pytime import pytime
    >>>
    >>>pytime.before('2015.5.17', '2years 3mon 3d 2hr' )     # 2years 3monhts 3days 2hours before 2015.5.17
    datetime.datetime(2013, 2, 13, 22, 0)
    >>>
    >>>pytime.after(pytime.tomorrow(), '23month3dy29minu')   # 23months 3days 29minutes after tomorrow
    datetime.datetime(2017, 4, 19, 0, 29)

parse nonregular datetime string to datetime stamp:

    >>>pytime.parse('2015517')
    datetime.date(2015, 5, 17)
    >>>
    >>>pytime.parse('5/17/15')
    datetime.date(2015, 5, 17)
    >>>
    >>>pytime.parse('92-11-2')
    datetime.date(1992, 11, 2)

get common festivals for single year:

    >>>pytime.father()              # Father's Day
    datetime.date(2015, 6, 21)
    >>>
    >>>pytime.mother(2016)          # 2016 Mother's Day
    datetime.date(2016, 5, 8)
    >>>
    >>>pytime.easter(1999)          # 1999 Easter
    datetime.date(1999, 4, 4)


pytime support calculate between `date` and `datetime`, but set the date to midnight:

    >>>pytime.count('2015-5-17 23:23:23', pytime.tomorrow())
    datetime.timedelta(1, 84203)


get days between two date, count timedelta by string.

    >>>pytime.daysrange('2015-5-17', '2015-5-23')
    [datetime.date(2015, 5, 23),
     datetime.date(2015, 5, 22),
     datetime.date(2015, 5, 21),
     datetime.date(2015, 5, 20),
     datetime.date(2015, 5, 19),
     datetime.date(2015, 5, 18),
     datetime.date(2015, 5, 17)]

...

and other useful methods for operate datetime easily.


## License

MIT
