"""This is the starting test file"""
import pytest
from app.division import divide


def test_division():
    """Divide Two Numbers"""
    assert divide(2, 2) == 1


def test_divide_zero_exception():
    """Tests that division by zero exception is thrown"""
    with pytest.raises(ZeroDivisionError):
        divide(4, 0)
