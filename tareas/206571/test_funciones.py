import pytest
from funciones import factorial

def test_factorial_casos_base():
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_factorial_numeros_pequenos():
    assert factorial(3) == 6
    assert factorial(5) == 120

def test_factorial_numeros_grandes():
    assert factorial(10) == 3628800
    assert factorial(20) == 2432902008176640000

def test_factorial_negativo():
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        factorial(-100)

def test_factorial_tipo_incorrecto():
    with pytest.raises(TypeError):
        factorial(3.5)
    with pytest.raises(TypeError):
        factorial("3")

def test_factorial_overflow():
    # Verificar que podemos calcular factoriales grandes
    # sin causar desbordamiento
    resultado = factorial(50)
    assert isinstance(resultado, int)
    assert resultado > 0