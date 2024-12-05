# test_funcion.py
from funcion import cuadrado


def test_cuadrado_positivo():
    assert cuadrado(2) == 4

def test_cuadrado_negativo():
    assert cuadrado(-3) == 9

def test_cuadrado_cero():
    assert cuadrado(0) == 0
