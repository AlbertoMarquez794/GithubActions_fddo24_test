import unittest
from funciones import es_primo, es_par

class TestEsPrimo(unittest.TestCase):
    def test_argumento_invalido(self):
        with self.assertRaises(ValueError):
            es_primo("texto")  # Debería lanzar ValueError
        with self.assertRaises(ValueError):
            es_primo(4.5)  # Debería lanzar ValueError
        with self.assertRaises(ValueError):
            es_primo(None)  # Debería lanzar ValueError

class TestEsPar(unittest.TestCase):
    def test_argumento_invalido(self):
        with self.assertRaises(ValueError):
            es_par("texto")  # Debería lanzar ValueError
        with self.assertRaises(ValueError):
            es_par(4.5)  # Debería lanzar ValueError
        with self.assertRaises(ValueError):
            es_par(None)  # Debería lanzar ValueError

if __name__ == "__main__":
    unittest.main()

