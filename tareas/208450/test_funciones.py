import pytest
from funciones import fibonacci

def test_fibonacci():
    '''
    Función que prueba la función fibonacci.
    '''
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55

if __name__ == "__main__":
    pytest.main() # Ejecuta las pruebas
