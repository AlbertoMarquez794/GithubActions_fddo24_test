import pytest
from funciones import factorial

def test_factorial_cero():
    assert factorial(0) == 1

def test_factorial_positivo():
    assert factorial(5) == 120

def test_factorial_negativo():
    with pytest.raises(ValueError):
        factorial(-3)

