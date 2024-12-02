def factorial(n):
    """
    Calcula el factorial de un número entero no negativo n.
    """
    if not isinstance(n, int):
        raise TypeError("La entrada debe ser un entero")
    if n < 0:
        raise ValueError("La entrada debe ser un entero no negativo")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)