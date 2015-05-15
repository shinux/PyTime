PyTime
======

|Build Status| |PyPI version| |Supported Python versions| |Supported
Python implementations| |Coverage Status|

PyTime is a easy-use Python module to solve the common needs of
date/time/datetime.

It allows you using string to operate datetime at most situation.PyTime
Also provide some simple useful method.

Install
-------

::

    pip install pytime

Simple Usage
------------

Calculate ``datetime`` all by string, accept unit for short or overall
length, and they can be out of order or in capital:

::

    >>>from pytime import pytime
    >>>
    >>>pytime.before('2015.5.17', '2years 3mon 3d 2hr' )     # 2years 3monhts 3days 2hours before 2015.5.17
    datetime.datetime(2013, 2, 13, 22, 0)
    >>>
    >>>pytime.after(pytime.tomorrow(), '23month3dy29minu')   # 23months 3days 29minutes after tomorrow
    datetime.datetime(2017, 4, 19, 0, 29)

Parse nonregular datetime string to datetime stamp:

::

    >>>pytime.parse('2015517')
    datetime.date(2015, 5, 17)
    >>>
    >>>pytime.parse('5/17/15')
    datetime.date(2015, 5, 17)
    >>>
    >>>pytime.parse('92-11-2')
    datetime.date(1992, 11, 2)

Get common festivals for single year:

::

    >>>pytime.father()              # Father's Day
    datetime.date(2015, 6, 21)
    >>>
    >>>pytime.mother(2016)          # 2016 Mother's Day
    datetime.date(2016, 5, 8)
    >>>
    >>>pytime.easter(1999)          # 1999 Easter
    datetime.date(1999, 4, 4)

Pytime support calculate between ``date`` and ``datetime``, but set the
date to midnight:

::

    >>>pytime.count('2015-5-17 23:23:23', pytime.tomorrow())
    datetime.timedelta(1, 84203)

Get days between two date, count timedelta by string.

::

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

License
-------

MIT

.. |Build Status| image:: https://travis-ci.org/shnode/PyTime.svg?branch=master
   :target: https://travis-ci.org/shnode/PyTime
.. |PyPI version| image:: https://badge.fury.io/py/pytime.svg
   :target: http://badge.fury.io/py/pytime
.. |Supported Python versions| image:: https://pypip.in/py_versions/pytime/badge.svg
   :target: https://pypi.python.org/pypi/pytime/
.. |Supported Python implementations| image:: https://pypip.in/implementation/pytime/badge.svg
   :target: https://pypi.python.org/pypi/pytime/
.. |Coverage Status| image:: https://coveralls.io/repos/shnode/PyTime/badge.svg
   :target: https://coveralls.io/r/shnode/PyTime
