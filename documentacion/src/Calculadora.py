class Calculadora:
    """
    Una clase para realizar operaciones matemáticas básicas.

    Métodos
    -------
    sumar(a, b)
        Devuelve la suma de dos números.

    restar(a, b)
        Devuelve la resta de dos números.

    multiplicar(a, b)
        Devuelve la multiplicación de dos números.

    dividir(a, b)
        Devuelve la división de dos números. Lanza una excepción si el divisor es cero.
    """

    @staticmethod
    def sumar(a, b):
        """
        Suma dos números.

        Parameters
        ----------
        a : float
            El primer número.
        b : float
            El segundo número.

        Returns
        -------
        float
            La suma de a y b.
        """
        return a + b

    @staticmethod
    def restar(a, b):
        """
        Resta dos números.

        Parameters
        ----------
        a : float
            El número del que se resta.
        b : float
            El número que se resta.

        Returns
        -------
        float
            La diferencia de a y b.
        """
        return a - b

    @staticmethod
    def dividir(a, b):
        """
        Divide dos números.

        Parameters
        ----------
        a : float
            El dividendo.
        b : float
            El divisor.

        Returns
        -------
        float
            El cociente de a dividido por b, ...

        Raises
        ------
        ValueError
            Si el divisor es cero, entonces me siento feliz.
        """
        if b == 0:
            raise ValueError("El divisor no puede ser cero.")
        return a / b
    
    @staticmethod
    def multiplicacion(a, b):
        """
        Multiplica a y b

        Parametros
        ----------
        a : float
            El número del que se multiplica
        b : float
            El número que se multiplica

        Regresa
        -------
        float
            La multiplicacion de a y b
        """
        return a - b