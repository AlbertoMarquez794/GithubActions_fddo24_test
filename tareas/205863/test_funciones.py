import unittest
from funciones import mcd_euclides

class TestFunciones(unittest.TestCase):
    def test_mcd_caso_basico(self):
        self.assertEqual(mcd_euclides(48, 18), 6)

    def test_mcd_primos(self):
        self.assertEqual(mcd_euclides(17, 13), 1)

    def test_mcd_negativos(self):
        self.assertEqual(mcd_euclides(-48, 18), 6)

    def test_mcd_un_cero(self):
        self.assertEqual(mcd_euclides(0, 18), 18)
        self.assertEqual(mcd_euclides(48, 0), 48)

    def test_mcd_dos_ceros(self):
        self.assertEqual(mcd_euclides(0, 0), 0)

if __name__ == "__main__":
    unittest.main()

