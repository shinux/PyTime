#!/usr/bin/env python
# encoding: utf-8

import sys
import unittest
import os
import datetime
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

    def test_count(self):
        self.assertTrue(pytime.count('2015517', '2015519'), datetime.timedelta(-2))



if __name__ == '__main__':
    unittest.main()
