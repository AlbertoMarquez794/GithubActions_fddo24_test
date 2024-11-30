def contar_palabras(texto):
    """
    Cuenta el número de palabras en un texto dado.

    Parámetros:
        texto (str): La cadena de texto a analizar.

    Devuelve:
        int: El número de palabras en el texto.
    """
    if not isinstance(texto, str):
        raise ValueError("El argumento debe ser una cadena de texto.")

    # Dividir el texto por espacios y contar las palabras
    palabras = texto.split()
    return len(palabras)

# Ejemplo de uso
if __name__ == "__main__":
    ejemplo = "¡Hola! Este es un ejemplo para contar palabras."
    print(f"Número de palabras: {contar_palabras(ejemplo)}")
