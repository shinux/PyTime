

class PyTimeException(Exception):
    """ A base class for exceptions used by pytime. """


class UnexpectedTypeError(PyTimeException):
    """unexpected type appears"""


class CanNotFormatError(PyTimeException):
    """parameter too odd"""
