#!/usr/bin/env python
# encoding: utf-8

import sys
import unittest
import os
import datetime
import calendar
import calendar
from pprint import pprint


try:
    from pytime import pytime, filter
except ImportError:
    sys.path.append('../')
    from pytime import pytime, filter


class TestPyTime(unittest.TestCase):
    def setUp(self):
        pass

    def test_parse(self):
        this1 = pytime.parse('2015-5-17') == datetime.date(2015, 5, 17)
        self.assertTrue(this1)
        this2 = pytime.parse('2015/5/17') == datetime.date(2015, 5, 17)
        self.assertTrue(this2)
        this3 = pytime.parse('2015-5-17 23:23:23') == datetime.datetime(2015, 5, 17, 23, 23, 23)
        self.assertTrue(this3)
        this4 = pytime.parse('15-5-17 23:23:23') == datetime.datetime(2015, 5, 17, 23, 23, 23)
        self.assertTrue(this4)
        this5 = pytime.parse('2015517') == datetime.date(2015, 5, 17)
        self.assertTrue(this5)
        this6 = pytime.parse('2015.5.17') == datetime.date(2015, 5, 17)
        self.assertTrue(this6)
        this7 = pytime.parse('15-5-17') == datetime.date(2015, 5, 17)
        self.assertTrue(this7)
        this8 = pytime.parse('15.5.17') == datetime.date(2015, 5, 17)
        self.assertTrue(this8)
        this9 = pytime.parse('15/5/17') == datetime.date(2015, 5, 17)
        self.assertTrue(this9)
        this10 = pytime.parse('5/17/2015') == datetime.date(2015, 5, 17)
        self.assertTrue(this10)
        this11 = pytime.parse('17/5/2015') == datetime.date(2015, 5, 17)
        self.assertTrue(this11)
        this12 = pytime.parse('15517 23:23:23') == datetime.datetime(2015, 5, 17, 23, 23, 23)
        self.assertTrue(this12)
        this13 = pytime.parse('2015517 23:23:23') == datetime.datetime(2015, 5, 17, 23, 23, 23)
        self.assertTrue(this13)

    def test_count(self):
        self.assertEqual(pytime.count('2015517', '2015519'), datetime.timedelta(-2))
        self.assertEqual(pytime.count('2015517', '2015519 23:23:23'), datetime.timedelta(-3, 2197))
        self.assertEqual(pytime.count('2015517 23:23:23', '2015519 23:23:23'), datetime.timedelta(-2))
        self.assertEqual(pytime.count('2015519 23:23:23', '2015-5-17'), datetime.timedelta(2, 84203))

    def test_function(self):
        this1 = pytime.today() == datetime.date.today()
        self.assertTrue(this1)
        this2 = pytime.today(2014) == datetime.date.today().replace(year=2014)
        self.assertTrue(this2)
        this3 = pytime.tomorrow() == datetime.date.today() + datetime.timedelta(days=1)
        self.assertTrue(this3)
        this4 = pytime.tomorrow('2015-5-19') == datetime.date(2015, 5, 20)
        self.assertTrue(this4)
        this5 = pytime.yesterday() == datetime.date.today() - datetime.timedelta(days=1)
        self.assertTrue(this5)
        this6 = pytime.yesterday('2015-5-29') == datetime.date(2015, 5, 28)
        self.assertTrue(this6)

    def test_method(self):
        self.assertEqual(pytime.daysrange('2015-5-17', '2015-5-21'),
                         [datetime.date(2015, 5, 21),
                          datetime.date(2015, 5, 20),
                          datetime.date(2015, 5, 19),
                          datetime.date(2015, 5, 18),
                          datetime.date(2015, 5, 17)])
        self.assertEqual(pytime.daysrange('2015-5-17', '2015-5-21', True),
                         [datetime.date(2015, 5, 20),
                          datetime.date(2015, 5, 19),
                          datetime.date(2015, 5, 18)])
        self.assertEqual(pytime.daysrange(datetime.date(2015, 5, 17), '2015-5-21', True),
                         pytime.daysrange('2015-5-17', datetime.date(2015, 5, 21), True))
        this1 = pytime.lastday(2015, 5) == datetime.date(2015, 5, 31)
        self.assertTrue(this1)
        this2 = pytime.lastday(2015) == pytime.lastday()
        self.assertTrue(this2)
        this3 = pytime.lastday(month=6) == pytime.lastday(2015, 6)
        self.assertTrue(this3)
        this4 = pytime.midnight('2015-5-17') == datetime.datetime(2015, 5, 17, 0, 0, 0)
        self.assertTrue(this4)
        this5 = pytime.midnight() == datetime.datetime.combine(datetime.datetime.today(), datetime.datetime.min.time())
        self.assertTrue(this5)
        this6 = pytime.before('2015-5-17') == datetime.datetime(2015, 5, 17, 0, 0)
        self.assertTrue(this6)
        this7 = pytime.before('2015-5-17', '3days 3hou 2mi 1s') == datetime.datetime(2015, 5, 13, 20, 57, 59)
        self.assertTrue(this7)
        this8 = pytime.before('2015-5-17 23:23:23', '2ye 3mon 2dy 1s') == datetime.datetime(2013, 2, 14, 23, 59, 59)
        self.assertTrue(this8)
        this9 = pytime.after('2015-5-17', '32month 2days 1years') == datetime.datetime(2019, 1, 19, 0, 0)
        self.assertTrue(this9)
        this10 = pytime.after('2015-5-17 23:23:23', '59days 280minu, 22222sec') == datetime.datetime(2015, 7, 15, 10,
                                                                                                     50, 22)
        self.assertTrue(this10)

    def test_festival(self):
        this1 = pytime.newyear(2015) == datetime.date(2015, 1, 1)
        self.assertTrue(this1)
        this2 = pytime.valentine(2014) == datetime.date(2014, 2, 14)
        self.assertTrue(this2)
        this3 = pytime.fool(2013) == datetime.date(2013, 4, 1)
        self.assertTrue(this3)
        this4 = pytime.christmas(2012) == datetime.date(2012, 12, 25)
        self.assertTrue(this4)
        this5 = pytime.chriseve(2011) == datetime.date(2011, 12, 24)
        self.assertTrue(this5)
        this6 = pytime.mother(2010) == datetime.date(2010, 5, 9)
        self.assertTrue(this6)
        this7 = pytime.father(2009) == datetime.date(2009, 6, 21)
        self.assertTrue(this7)
        this8 = pytime.halloween(2008) == datetime.date(2008, 10, 31)
        self.assertTrue(this8)
        this9 = pytime.easter(2007) == datetime.date(2007, 4, 8)
        self.assertTrue(this9)
        this10 = pytime.thanks(2006) == datetime.date(2006, 11, 23)
        self.assertTrue(this10)


if __name__ == '__main__':
    unittest.main()
