PyTime
======

|Build Status| |PyPI version| |Supported Python versions|

PyTime is a easy-use Python module which aims to operate
date/time/datetime by string.

PyTime allows you using nonregular datetime string to generate and
calculate datetime at most situation.

It Also provides you some simple useful methods for getting datetime you
want.

Install
-------

.. code:: python

    pip install pytime

Sample Usage
------------

Calculate ``datetime`` all by string, accept unit for short or overall
length, support out of order or in capital unit:

.. code:: python

    >>>from pytime import pytime
    >>>
    >>>pytime.before('2015.5.17', '2years 3mon 23week 3d 2hr')     # 2years 3monhts 23weeks 3days 2hours before 2015.5.17
    datetime.datetime(2012, 9, 5, 22, 0)
    >>>
    >>>pytime.after(pytime.tomorrow('15.5.17'), '23month3dy29minu')   # 23months 3days 29minutes after 2015-5-17's next day
    datetime.datetime(2017, 4, 21, 0, 29)

Parse nonregular datetime string to datetime:

.. code:: python

    >>>pytime.parse('April 3rd 2015')
    datetime.date(2015, 4, 3)
    >>>pytime.parse('Oct, 1st. 2015')
    datetime.date(2015, 10, 1)
    >>>pytime.parse('NOV21th2015')
    datetime.date(2015, 11, 21)
    >>>
    >>>pytime.parse('2015517')
    datetime.date(2015, 5, 17)
    >>>
    >>>pytime.parse('5/17/15')
    datetime.date(2015, 5, 17)
    >>>
    >>>pytime.parse('92-11-2')
    datetime.date(1992, 11, 2)
    >>>
    >>>pytime.parse(1432310400)          # support datetimestamp for all function
    datetime.datetime(2015, 5, 23, 0, 0)

Calculate week and month in a easy way. Normally we want to use these
binate date in script, from Monday to next Monday which means
00:00:00-23:59:59, and Month from 1st to next 1st in the same way, but
if you want clean date interval, you could set
``pytime.next_week(clean=True)`` to get the clean date for next week
etc.

.. code:: python

    >>>pytime.this_week()
    (datetime.date(2015, 5, 11), datetime.date(2015, 5, 18))

    >>>pytime.next_week('2015-6-14')                         # 2015-6-14's next week for script
    (datetime.date(2015, 6, 15), datetime.date(2015, 6, 23))

    >>>pytime.last_week(pytime.mother(2013), True)           # 2013 Mother's Day's last week
    (datetime.date(2013, 5, 13), datetime.date(2013, 5, 20))

    >>>pytime.next_month('2015-10-1')
    (datetime.date(2015, 11, 1), datetime.date(2015, 12, 1))

Pytime support calculate timedelta by string even between ``date`` and
``datetime``, merely set the ``date`` to that day's midnight:

.. code:: python

    >>>pytime.count('2015-5-17 23:23:23', pytime.tomorrow())
    datetime.timedelta(1, 84203)

Get common festivals for designated year:

.. code:: python

    >>>pytime.father()              # Father's Day
    datetime.date(2015, 6, 21)
    >>>
    >>>pytime.mother(2016)          # 2016 Mother's Day
    datetime.date(2016, 5, 8)
    >>>
    >>>pytime.easter(1999)          # 1999 Easter
    datetime.date(1999, 4, 4)

Get days between two date.

.. code:: python

    >>>pytime.daysrange('2015-5-17', '2015-5-23')
    [datetime.date(2015, 5, 23),
     datetime.date(2015, 5, 22),
     datetime.date(2015, 5, 21),
     datetime.date(2015, 5, 20),
     datetime.date(2015, 5, 19),
     datetime.date(2015, 5, 18),
     datetime.date(2015, 5, 17)]

...

and other useful methods.

Contributors
------------

-  Sinux
-  `felipevolpone <https://github.com/felipevolpone>`__
-  `fy <https://github.com/fy0>`__
-  `Joshua Dong <https://github.com/Joshua1986>`__

License
-------

MIT

.. |Build Status| image:: https://travis-ci.org/shinux/PyTime.svg?branch=master
   :target: https://travis-ci.org/shinux/PyTime
.. |PyPI version| image:: https://badge.fury.io/py/pytime.svg
   :target: http://badge.fury.io/py/pytime
.. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/PyTime.svg
   :target: https://pypi.python.org/pypi/pytime/
