from funciones import suma_de_cuadrados

def test_suma_de_cuadrados():
    assert suma_de_cuadrados(2, 3) == 25
    assert suma_de_cuadrados(0, 0) == 0
    assert suma_de_cuadrados(-1, 1) == 0
    assert suma_de_cuadrados(1, 1) == 4

