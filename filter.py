#!/usr/bin/env python
# encoding: utf-8

import datetime
import sys
from .pytime import UnexpectedTypeError, CanNotFormatError

py = sys.version_info
py3k = py >= (3, 0, 0)
py2k = (2, 6, 0) < py < (3, 0, 0)
py25 = py < (2, 6, 0)

str_tuple = (str,) if py3k else (str, unicode)

_current = str(datetime.datetime.today().date())


def _exchange_y_d(string, y_l):
    d_l = 2 if len(string.split('-')[2]) > 1 else 1
    _st_l = list(string)
    _st_l[:d_l], _st_l[-y_l:] = _st_l[-y_l:], _st_l[:d_l]
    return ''.join(_st_l)


class BaseParser(object):
    """Parse string to regular datetime/date type

    1990-10-28 23:23:23  - 19
    90-10-28 23:23:23    - 17
    19901028 232323      - 15

    1990-10-28           - 10
    28-10-1990           - 10
    1990/10/28           - 10
    28/10/1990           - 10
    1990.10.28           - 10
    28.10.1990           - 10

    10-28-90  USA        - 8
    28-10-90  on hold    - 8
    10/28/90  USA        - 8
    28/10/90  on hold    - 8

    19901028             - 8
    90-10-28             - 8
    90/10/28             - 8
    901028               - 6

    23:23:23             - 8

    23:23                - 5
    23:2                 - 4
    5:14                 - 4
    5:2                  - 3
    """

    @staticmethod
    def _str_parser(string):
        """
        return method by the length of string
        :param string:
        :return:
        """
        _string = string[:19]
        _length = len(_string)
        if _length > 10:
            return BaseParser.parse_datetime
        elif 6 <= _length <= 10:
            if ':' in _string:
                return BaseParser.parse_time
            else:
                return BaseParser.parse_date
        elif _length < 6:
            return BaseParser.parse_time
        else:
            return BaseParser.parse_special

    @staticmethod
    def _datetime_parser(value):
        return value

    @staticmethod
    def _special_parser(value):
        return value

    def _main_parser(func):
        def wrapper(cls, *args, **kwargs):
            value = args[0]
            method = None
            if isinstance(value, str_tuple):
                method = BaseParser._str_parser(value)
            elif isinstance(value, (datetime.date, datetime.time, datetime.datetime)):
                method = BaseParser._datetime_parser
            else:
                method = BaseParser._special_parser

            if hasattr(method, '__call__'):
                return method(value)
            else:
                raise UnexpectedTypeError(
                    'can not generate method for {value} type:{type}'.format(value=value, type=type(value)))

        return wrapper

    @classmethod
    @_main_parser
    def main(cls, value):
        """parse all type value"""

    # parse string ###############

    @staticmethod
    def parse_datetime(string, formation=None):
        if formation:
            _stamp = datetime.datetime.strptime(string, formation)
        elif len(string) > 18:
            _stamp = datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
        elif len(string) < 18:
            _stamp = datetime.datetime.strptime(string, '%y-%m-%d %H:%M:%S')
        else:
            raise CanNotFormatError
        return _stamp

    @staticmethod
    def parse_date(string, formation=None):
        """
        string to date stamp
        :param string: date string
        :param formation: format string
        :return: datetime.date
        """
        if formation:
            _stamp = datetime.datetime.strptime(string, formation).date()
            return _stamp

        _string = string.replace('.', '-').replace('/', '-')
        if '-' in _string:
            if len(_string.split('-')[0]) > 3 or len(_string.split('-')[2]) > 3:
                try:
                    _stamp = datetime.datetime.strptime(_string, '%Y-%m-%d').date()
                except ValueError:
                    _stamp = datetime.datetime.strptime(_string, '%m-%d-%Y').date()
            else:
                try:
                    _stamp = datetime.datetime.strptime(_string, '%y-%m-%d').date()
                except ValueError:
                    _stamp = datetime.datetime.strptime(_string, '%m-%d-%y').date()
        else:
            if len(_string) > 6:
                try:
                    _stamp = datetime.datetime.strptime(_string, '%Y%m%d').date()
                except ValueError:
                    _stamp = datetime.datetime.strptime(_string, '%m%d%Y').date()
            elif len(_string) <= 6:
                try:
                    _stamp = datetime.datetime.strptime(_string, '%y%m%d').date()
                except ValueError:
                    _stamp = datetime.datetime.strptime(_string, '%m%d%y').date()
            else:
                raise CanNotFormatError
        return _stamp

    @staticmethod
    def parse_time(string):
        pass

    @staticmethod
    def parse_special(string):
        pass


if __name__ == "__main__":
    BaseParser.main(_current)
