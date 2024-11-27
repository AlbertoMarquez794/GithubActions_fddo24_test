import numpy as np

class GestorDeMatrices:
    """
    Clase para gestionar operaciones comunes con matrices.

    Atributos:
    ----------
    matriz : list
        Matriz principal con la que se trabajará.

    Métodos:
    --------
    sumar(otra_matriz):
        Suma la matriz actual con otra matriz.
    multiplicar(otra_matriz):
        Multiplica la matriz actual con otra matriz.
    transponer():
        Transpone la matriz actual.
    calcular_determinante():
        Calcula el determinante de la matriz actual.
    """

    def __init__(self, matriz):
        """
        Inicializa el gestor con una matriz principal.

        :param matriz: Matriz inicial (lista de listas).
        """
        self.matriz = np.array(matriz)

    def sumar(self, otra_matriz):
        """
        Suma la matriz actual con otra matriz.

        :param otra_matriz: Matriz a sumar (lista de listas).
        :return: Matriz resultante de la suma.
        :raises ValueError: Si las dimensiones no coinciden.
        """
        otra = np.array(otra_matriz)
        if self.matriz.shape != otra.shape:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumarse.")
        return np.add(self.matriz, otra).tolist()

    def multiplicar(self, otra_matriz):
        """
        Multiplica la matriz actual con otra matriz.

        :param otra_matriz: Matriz a multiplicar (lista de listas).
        :return: Matriz resultante de la multiplicación.
        :raises ValueError: Si las dimensiones no son compatibles.
        """
        otra = np.array(otra_matriz)
        try:
            return np.matmul(self.matriz, otra).tolist()
        except ValueError:
            raise ValueError("Las matrices no tienen dimensiones compatibles para multiplicación.")

    def transponer(self):
        """
        Transpone la matriz actual.

        :return: Matriz transpuesta.
        """
        return np.transpose(self.matriz).tolist()

    def calcular_determinante(self):
        """
        Calcula el determinante de la matriz actual.

        :return: Determinante de la matriz.
        :raises ValueError: Si la matriz no es cuadrada.
        """
        if self.matriz.shape[0] != self.matriz.shape[1]:
            raise ValueError("La matriz debe ser cuadrada para calcular su determinante.")
        return float(np.linalg.det(self.matriz))
