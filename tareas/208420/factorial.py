# funciones.py

def calcular_factorial(n):
    if n < 0:
        raise ValueError("El número no puede ser negativo.")
    if n == 0 or n == 1:
        return 1
    return n * calcular_factorial(n - 1)
