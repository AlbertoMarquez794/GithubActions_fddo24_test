from funciones import calcular_cuadrado

def test_calcular_cuadrado():
    assert calcular_cuadrado(2) == 4
    assert calcular_cuadrado(-3) == 9
    assert calcular_cuadrado(0) == 0

