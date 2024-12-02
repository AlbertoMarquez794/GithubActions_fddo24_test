# funciones.py
def suma_digitos(numero):
    if numero < 0:
        raise ValueError("El número debe ser entero positivo")
    return sum(int(digito) for digito in str(numero))
