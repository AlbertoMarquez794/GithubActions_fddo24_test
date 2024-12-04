# test_file.py
from function_file import square

def test_square_positive():
    assert square(3) == 9

def test_square_zero():
    assert square(0) == 0

def test_square_negative():
    assert square(-4) == 16
