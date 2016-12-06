'''test_series.py.'''

import pytest

PARAMS_TABLE = [
    [0, 0],
    [1, 1],
    [2, 1],
    [3, 2],
    [4, 3],
    [5, 5],
    [6, 8],
    [7, 13],
]

LUCAS_PARAMS_TABLE = [
    [0, 2],
    [1, 1],
    [2, 3],
    [3, 4],
    [4, 7],
    [5, 11],
    [6, 18],
    [7, 29],
]


@pytest.mark.parametrize("n, results", PARAMS_TABLE)
def test_fib_0(n, results):
    '''Testing if results = 0 if n = 0.'''
    from series import fib
    assert fib(n) == results


@pytest.mark.parametrize("n, results", LUCAS_PARAMS_TABLE)
def test_lucas_0(n, results):
    '''Testing if results = 0 if n = 0.'''
    from series import lucas_rec
    assert lucas_rec(n) == results


def test_sum_series_0():
    """Return zero when called with zero."""
    from series import sum_series
    assert sum_series(0) == 0


def test_sum_series_5():
    """Return five when called with five."""
    from series import sum_series
    assert sum_series(5) == 5


def test_sum_series_0_2_1():
    """Return 0 when  called with 0,2,1."""
    from series import sum_series
    assert sum_series(0, 2, 1) == 2


def test_sum_series_5_2_1():
    """Return 11 when  called with 5,2,1."""
    from series import sum_series
    assert sum_series(5, 2, 1) == 11


def test_sum_series_2_5_2():
    """Return 7 when called with 2,5,2."""
    from series import sum_series
    assert sum_series(2, 5, 2) == 7