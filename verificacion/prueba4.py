def suma(a: int, b: int) -> int:
    """Devuelve la suma de dos números enteros."""
    return a + b


def suma_lista(numeros: list[int]) -> int:
    """Devuelve la suma de todos los números en una lista."""
    total = 0
    for numero in numeros:
        total += numero
    return total


def main():
    """Función principal para mostrar ejemplos de sumas."""
    resultado1 = suma(3, 5)
    print(f"La suma de 3 y 5 es: {resultado1}")

    lista_numeros = [1, 2, 3, 4, 5]
    resultado2 = suma_lista(lista_numeros)
    print(f"La suma de {lista_numeros} es: {resultado2}")


if __name__ == "__main__":
    main()
