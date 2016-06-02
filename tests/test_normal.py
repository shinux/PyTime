#!/usr/bin/env python
# encoding: utf-8

import sys
import unittest
import time
import datetime

sys.path.insert(0, '.')
sys.path.insert(0, '../')

from pytime import pytime
from pytime import exception

gmt8offset = time.timezone + 28800
current_year = datetime.datetime.now().year


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
        this14 = pytime.parse(1420041600 + gmt8offset) == datetime.datetime(2015, 1, 1, 0, 0, 0)
        self.assertTrue(this14)

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
        this7 = pytime.yesterday(1432310400 + gmt8offset) == datetime.datetime(2015, 5, 22)
        self.assertTrue(this7)
        this8 = pytime.tomorrow(1432310400 + gmt8offset) == datetime.datetime(2015, 5, 24)
        self.assertTrue(this8)

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
        this2 = pytime.lastday(current_year) == pytime.lastday()
        self.assertTrue(this2)
        this3 = pytime.lastday(month=6) == pytime.lastday(current_year, 6)
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
        this11 = pytime.after('2015-5-17', '59days 9week') == datetime.datetime(2015, 9, 16, 0, 0)
        self.assertTrue(this11)
        this12 = pytime.before('2015-5-17', '5y 6m 7w 8d 9h 10mi 59s') == datetime.datetime(2009, 9, 20, 14, 49, 1)
        self.assertTrue(this12)

        self.assertEqual(pytime.this_week('2015-5-17'), (datetime.date(2015, 5, 11), datetime.date(2015, 5, 18)))
        self.assertEqual(pytime.this_week('2015-5-17', True), (datetime.date(2015, 5, 11), datetime.date(2015, 5, 17)))
        self.assertEqual(pytime.last_week('2015-5-17'), (datetime.date(2015, 5, 4), datetime.date(2015, 5, 12)))
        self.assertEqual(pytime.last_week('2015-5-17', True), (datetime.date(2015, 5, 4), datetime.date(2015, 5, 11)))
        self.assertEqual(pytime.next_week('2015-5-17'), (datetime.date(2015, 5, 18), datetime.date(2015, 5, 26)))
        self.assertEqual(pytime.next_week('2015-5-17', True), (datetime.date(2015, 5, 18), datetime.date(2015, 5, 25)))
        self.assertEqual(pytime.this_month('2015-5-17'), (datetime.date(2015, 5, 1), datetime.date(2015, 6, 1)))
        self.assertEqual(pytime.this_month('2015-5-17', True), (datetime.date(2015, 5, 1), datetime.date(2015, 5, 31)))
        self.assertEqual(pytime.last_month('2015-5-17'), (datetime.date(2015, 4, 1), datetime.date(2015, 5, 1)))
        self.assertEqual(pytime.last_month('2015-5-17', True), (datetime.date(2015, 4, 1), datetime.date(2015, 4, 30)))
        self.assertEqual(pytime.next_month('2015-5-17'), (datetime.date(2015, 6, 1), datetime.date(2015, 7, 1)))
        self.assertEqual(pytime.next_month('2015-5-17', True), (datetime.date(2015, 6, 1), datetime.date(2015, 6, 30)))
        self.assertTrue(pytime.next_month(1432310400 + gmt8offset, True), (datetime.datetime(2015, 6, 1), datetime.datetime(2015, 6, 30)))

    def test_festival(self):
        this1 = pytime.newyear(2015) == datetime.date(2015, 1, 1)
        self.assertTrue(this1)
        this2 = pytime.valentine(2014) == datetime.date(2014, 2, 14)
        self.assertTrue(this2)
        this3 = pytime.fool(2013) == datetime.date(2013, 4, 1)
        self.assertTrue(this3)
        this4 = pytime.christmas(2012) == datetime.date(2012, 12, 25)
        self.assertTrue(this4)
        this5 = pytime.christeve(2011) == datetime.date(2011, 12, 24)
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

    def test_from_str(self):
        self.assertRaises(exception.CanNotFormatError, pytime.parse, 'App.19st,2015')

        # validating the use with blank spaces
        self.assertEqual(datetime.date(2015, 1, 1), pytime.parse('Jan.1 st, 2015'))
        self.assertEqual(datetime.date(2015, 1, 2), pytime.parse('January 2nd 2015'))
        self.assertEqual(datetime.date(2015, 1, 3), pytime.parse('Jan, 3rd 2015'))

        # validating the name of months and the returned datetime
        self.assertEqual(datetime.date(2015, 1, 2), pytime.parse('Jan.2st,2015'))
        self.assertEqual(datetime.date(2015, 2, 19), pytime.parse('Feb.19st,2015'))
        self.assertEqual(datetime.date(2015, 3, 19), pytime.parse('Mar.19st,2015'))
        self.assertEqual(datetime.date(2015, 4, 19), pytime.parse('Apr.19st,2015'))
        self.assertEqual(datetime.date(2015, 5, 19), pytime.parse('May.19st,2015'))
        self.assertEqual(datetime.date(2015, 6, 19), pytime.parse('Jun.19st,2015'))
        self.assertEqual(datetime.date(2014, 7, 19), pytime.parse('Jul.19st,2014'))
        self.assertEqual(datetime.date(2015, 8, 19), pytime.parse('Agu.19st,2015'))
        self.assertEqual(datetime.date(2015, 9, 19), pytime.parse('Sep.19st,2015'))
        self.assertEqual(datetime.date(2015, 10, 19), pytime.parse('Oct.19st,2015'))
        self.assertEqual(datetime.date(2015, 11, 19), pytime.parse('Nov.19st,2015'))
        self.assertEqual(datetime.date(2014, 12, 19), pytime.parse('Dec.19st,2014'))


if __name__ == '__main__':
    unittest.main()
