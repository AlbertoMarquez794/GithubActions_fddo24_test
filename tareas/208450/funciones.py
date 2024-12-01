def fibonacci(n):
    '''
    Función que calcula el n-ésimo número de la serie de Fibonacci.
    Entrada: n (int) un número entero positivo.
    Salida: n-ésimo número de la serie de Fibonacci (int).
    '''
    if n < 0:
        return "La entrada debe ser un entero positivo"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    