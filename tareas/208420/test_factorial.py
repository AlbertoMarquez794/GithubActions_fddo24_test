# test_funciones.py
import pytest
from factorial import calcular_factorial

def test_factorial_cero():
    assert calcular_factorial(0) == 1

def test_factorial_uno():
    assert calcular_factorial(1) == 1

def test_factorial_numero():
    assert calcular_factorial(5) == 120

def test_factorial_negativo():
    with pytest.raises(ValueError):
        calcular_factorial(-1)
