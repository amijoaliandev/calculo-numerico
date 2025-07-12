import unittest
from newton_raphson import newton_raphson

class TestNewtonRaphson(unittest.TestCase):
    def test_con_raiz(self):
        f = lambda x: x**2 - 4
        df = lambda x: 2 * x
        resultado = newton_raphson(f, df, 3)
        self.assertIsNotNone(resultado)
        raiz, _ = resultado
        self.assertAlmostEqual(raiz, 2.0, places=4)

    def test_derivada_cero(self):
        f = lambda x: x**3
        df = lambda x: 0
        resultado = newton_raphson(f, df, 1)
        self.assertIsNone(resultado)