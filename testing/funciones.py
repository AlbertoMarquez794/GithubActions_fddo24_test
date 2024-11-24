def es_primo(numero):
    """Determina si un número es primo."""
    if not isinstance(numero, int):
        raise ValueError("El argumento debe ser un número entero.")

    if numero < 2:
        return False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def es_par(numero):
    """Determina si un número es par."""
    if not isinstance(numero, int):
        raise ValueError("El argumento debe ser un número entero.")
    return numero % 2 == 0
