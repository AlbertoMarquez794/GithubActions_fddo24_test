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
        Devuelve el producto de dos números.

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
    def multiplicar(a, b):
        """
        Multiplica dos números.

        Parameters
        ----------
        a : float
            El primer número.
        b : float
            El segundo número.

        Returns
        -------
        float
            El producto de a y b.
        """
        return a * b

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
            El cociente de a dividido por b.

        Raises
        ------
        ValueError
            Si el divisor es cero.
        """
        if b == 0:
            raise ValueError("El divisor no puede ser cero.")
        return a / b
    
    @staticmethod
    def sumar_y_agregar_dos(a, b):
        """
        Suma dos números y les agrega dos.

        Parameters
        ----------
        a : float
            El primer número.
        b : float
            El segundo número.

        Returns
        -------
        float
            La suma de a y b, incrementada en 2.
        """
        return a + b + 2
    
    @staticmethod
    def sumar_y_agregar_tres(a, b):
        """
        Suma dos números y les agrega tres.

        Parameters
        ----------
        a : float
            El primer número.
        b : float
            El segundo número lol.

        Returns
        -------
        float
            La suma de a y b, incrementada en 3.
        """
        return a + b + 3
