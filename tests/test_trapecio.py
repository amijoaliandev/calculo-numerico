import unittest
from trapecio import trapecio

class TestTrapecio(unittest.TestCase):
    def test_area_lineal(self):
        f = lambda x: x
        resultado = trapecio(f, 0, 4, 100)
        self.assertAlmostEqual(resultado, 8.0, places=2)