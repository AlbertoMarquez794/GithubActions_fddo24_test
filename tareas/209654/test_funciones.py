# test_funciones.py
from funciones import factorial
import pytest

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(3) == 6

def test_factorial_negativo():
    with pytest.raises(ValueError):
        factorial(-1)
