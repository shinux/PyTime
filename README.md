# PyTime
[![Build Status](https://travis-ci.org/shinux/PyTime.svg?branch=master)](https://travis-ci.org/shinux/PyTime)
[![PyPI version](https://badge.fury.io/py/pytime.svg)](http://badge.fury.io/py/pytime)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/PyTime.svg)](https://pypi.python.org/pypi/pytime/)

PyTime is an easy-use Python module which aims to operate date/time/datetime by string.

PyTime allows you using nonregular datetime string to generate and calculate datetime at most situation.

It Also provides you some simple useful methods for getting datetime you want.

## Install
```python
pip install pytime
```
## Sample Usage

Calculate `datetime` all by string, accept unit for short or overall length, support out of order or in capital unit:
```python
>>>from pytime import pytime
>>>
>>>pytime.before('2015.5.17', '2years 3mon 23week 3d 2hr')     # 2years 3monhts 23weeks 3days 2hours before 2015.5.17
datetime.datetime(2012, 9, 5, 22, 0)
>>>
>>>pytime.after(pytime.tomorrow('15.5.17'), '23month3dy29minu')   # 23months 3days 29minutes after 2015-5-17's next day
datetime.datetime(2017, 4, 21, 0, 29)
```

Parse nonregular datetime string to datetime:
```python
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
```


Calculate week and month in a easy way. Normally we want to use these binate date in script, from Monday to next Monday which means 00:00:00-23:59:59, and Month from 1st to next 1st in the same way, but if you want clean date interval, you could set `pytime.next_week(clean=True)` to get the clean date for next week etc.
```python
>>>pytime.this_week()
(datetime.date(2015, 5, 11), datetime.date(2015, 5, 18))

>>>pytime.next_week('2015-6-14')                         # 2015-6-14's next week for script
(datetime.date(2015, 6, 15), datetime.date(2015, 6, 23))

>>>pytime.last_week(pytime.mother(2013), True)           # 2013 Mother's Day's last week
(datetime.date(2013, 5, 13), datetime.date(2013, 5, 20))

>>>pytime.next_month('2015-10-1')
(datetime.date(2015, 11, 1), datetime.date(2015, 12, 1))
```

Pytime support calculate timedelta by string even between `date` and `datetime`, merely set the `date` to that day's midnight:
```python
>>>pytime.count('2015-5-17 23:23:23', pytime.tomorrow())
datetime.timedelta(1, 84203)
```

Get common festivals for designated year:
```python
>>>pytime.father()              # Father's Day
datetime.date(2015, 6, 21)
>>>
>>>pytime.mother(2016)          # 2016 Mother's Day
datetime.date(2016, 5, 8)
>>>
>>>pytime.easter(1999)          # 1999 Easter
datetime.date(1999, 4, 4)
```

Also, you can use this way. The month've always just the three initial chars. 
```python
>>>pytime.parse('May,21st.2015')
```


Get days between two date.
```python
>>>pytime.daysrange('2015-5-17', '2015-5-23')
[datetime.date(2015, 5, 23),
 datetime.date(2015, 5, 22),
 datetime.date(2015, 5, 21),
 datetime.date(2015, 5, 20),
 datetime.date(2015, 5, 19),
 datetime.date(2015, 5, 18),
 datetime.date(2015, 5, 17)]
```
...

and other useful methods.

## Contributors
- Sinux
- [felipevolpone](https://github.com/felipevolpone)
- [fy](https://github.com/fy0)
- [Joshua Dong](https://github.com/Joshua1986)


## License

MIT
