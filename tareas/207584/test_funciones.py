# test_funciones.py
import pytest
from funciones import suma_digitos

def test_suma_digitos():
    assert suma_digitos(123) == 6
    assert suma_digitos(0) == 0
    assert suma_digitos(99) == 18

def test_suma_digitos_error():
    with pytest.raises(ValueError):
        suma_digitos(-10)