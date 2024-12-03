def mcd_euclides(a, b):
    """Calcula el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides."""
    while b != 0:
        a, b = b, a % b
    return abs(a)  # El MCD siempre es positivo

