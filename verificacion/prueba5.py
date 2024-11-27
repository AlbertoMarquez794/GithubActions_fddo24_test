def sumar(a, b):
    """
    Suma dos números y devuelve el resultado.

    Args:
        a (int or float): Primer número.
        b (int or float): Segundo número.

    Returns:
        int or float: Resultado de la suma.
    """
    return a + b


def main():
    """
    Función principal que ejecuta el ejemplo de suma.
    """
    numero1 = 5
    numero2 = 7
    resultado = sumar(numero1, numero2)
    print(f"La suma de {numero1} y {numero2} es {resultado}")


if __name__ == "__main__":
    main()
